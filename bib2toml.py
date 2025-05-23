import re
import sys
import time
from datetime import datetime
from pybtex.database.input import bibtex
import toml
from pathlib import Path

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def print_error(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] ❌ Error: {message}", file=sys.stderr)

# Input/Output paths
bib_path = Path("publications.bib")
toml_path = Path("data/publications.toml")

# Compile regex patterns once for performance
latex_patterns = [
    (re.compile(pattern), replacement)
    for pattern, replacement in {
        r'~': ' ',
        r'\\ ': ' ',
        r'\\,': ' ',
        r'\\&': '&',
        r'\\%': '%',
        r'\\texttt{([^}]*)}': r'\1',
        r'\\textit{([^}]*)}': r'\1',
        r'\\emph{([^}]*)}': r'\1',
        r'\\textbf{([^}]*)}': r'\1',
        r'{([^}]*)}': r'\1',
        r'{\\[a-zA-Z]+\s+([^}]*)}': r'\1',  # matches {\LaTeX} or similar
    }.items()
]

def clean_latex(text):
    if not text:
        return ""
    cleaned = text
    for pattern, repl in latex_patterns:
        cleaned = pattern.sub(repl, cleaned)
    return cleaned.strip('{} ')

# Main processing function
def process_bibtex_to_toml():
    start_time = time.time()
    log_message("📖 Starting BibTeX to TOML conversion")

    try:
        # Check if BibTeX file exists
        if not bib_path.exists() or not bib_path.is_file():
            raise FileNotFoundError(f"Input BibTeX file not found at {bib_path}")

        # Load BibTeX entries with timing
        log_message("📖 Parsing BibTeX file...")
        parse_start = time.time()
        parser = bibtex.Parser()
        bib_data = parser.parse_file(bib_path)
        log_message(f"⏱️ BibTeX parsing completed in {time.time() - parse_start:.2f} seconds")

        publications = []

        # Cache frequently used mappings
        type_mapping = {
            "article": "Journal",
            "inproceedings": "Conference",
            "conference": "Conference",
            "inbook": "Chapter"
        }

        # Process each entry with timing
        process_start = time.time()
        for key, entry in bib_data.entries.items():
            fields = entry.fields

            # Check for required fields quickly
            title = fields.get("title")
            if not title:
                print_error(f"Missing 'title' field in entry: {key}")
                continue

            people = entry.persons.get("author", [])
            authors = [
                clean_latex((" ".join(p.first_names) if p.first_names else "")+" "+" ".join(p.last_names))
                for p in people
            ]

            if not authors:
                print_error(f"No authors found in entry: {key}")
                continue

            # Use cached mapping
            pub_type = type_mapping.get(entry.type.lower(), "Pre-print")

            # Build publication dictionary efficiently
            pub = {
                "title": clean_latex(title),
                "authors": authors,
                "year": int(fields.get("year", "1900")),
                "type": pub_type,
                "venue": clean_latex(fields.get("journal") or fields.get("booktitle") or fields.get("series") or "Unknown"),
                "bibtex": entry.to_string("bibtex")
            }

            # Add optional links efficiently
            links = []
            if "doi" in fields:
                links.append({"name": "DOI", "url": f"https://doi.org/{fields['doi']}"})
            if "url" in fields:
                links.append({"name": "URL", "url": fields["url"]})

            # Add optional media
            if "pdf" in fields:
                pub["pdf"] = fields["pdf"]
            if "video" in fields:
                pub["video"] = fields["video"]

            if links:
                pub["links"] = links

            publications.append(pub)

        log_message(f"⏱️ Processed {len(publications)} entries in {time.time() - process_start:.2f} seconds")

        # Output to TOML with timing
        toml_data = {"publications": publications}
        try:
            log_message("💾 Writing TOML data...")
            write_start = time.time()
            toml_path.parent.mkdir(parents=True, exist_ok=True)
            toml_path.write_text(toml.dumps(toml_data), encoding="utf-8")
            log_message(f"⏱️ TOML writing completed in {time.time() - write_start:.2f} seconds")
            return True
        except Exception as e:
            print_error(f"Failed to write TOML file: {e}")
            return False

    except FileNotFoundError as fnf_error:
        print_error(str(fnf_error))
    except Exception as e:
        print_error(f"Unexpected error during processing: {e}")

    log_message(f"⏱️ Total execution time: {time.time() - start_time:.2f} seconds")
    return False

# Run the main function with timing
if __name__ == "__main__":
    log_message("Starting bib2toml.py script execution...")
    success = process_bibtex_to_toml()
    if success:
        log_message("✅ Successfully cleaned LaTeX and generated data/publications.toml from publications.bib")
    else:
        print_error("❌ Failed to generate TOML data")

# Team Section Enhancement

This document describes the enhanced team section that now includes both list and detailed individual pages for team members.

## Overview

The team section has been extended to provide:
1. **Team List View** (`/team/`) - Shows all team members in a grid layout
2. **Individual Team Member Pages** (`/team/[member-name]/`) - Detailed pages for each team member

## File Structure

```
content/team/
├── _index.md                    # Team list page content
├── witold_bolt.md              # Individual team member pages
├── anna_nenca.md
├── adam_dzedzej.md
├── aleksander_bolt.md
├── antoni_augustynowicz.md
├── barbara_wolnik.md
├── bartosz_makuracki.md
├── maciej_dziemianczuk.md
└── marcin_dembowski.md

data/team/
├── witold_bolt.toml            # Team member data files
├── anna_nenca.toml
├── adam_dzedzej.toml
├── aleksander_bolt.toml
├── antoni_augustynowicz.toml
├── barbara_wolnik.toml
├── bartosz_makuracki.toml
├── maciej_dziemianczuk.toml
└── marcin_dembowski.toml

layouts/team/
├── list.html                   # Template for team list page
└── single.html                 # Template for individual team member pages
```

## Data Structure

Each team member's information is stored in a TOML file in `data/team/`. The filename (without extension) becomes the URL slug for their individual page.

### Basic Information (Required)
```toml
first_name = "First Name"
last_name = "Last Name"
deg = "dr"                      # Optional degree
role = "Position Title"
affiliation = "Institution Name"
email = "email@example.com"
avatar = "photos/filename.jpg"
weight = 1                      # Sort order (lower numbers first)
```

### Detailed Information (Optional)
```toml
bio = """
Biography text supporting markdown formatting.
Can be multiple paragraphs.
"""

research_interests = [
  "Research Area 1",
  "Research Area 2"
]

education = [
  { degree = "Ph.D. in Field", institution = "University", year = "2020" }
]

experience = [
  { position = "Current Position", organization = "Organization", period = "2020 - Present", description = "Description" }
]

publications_highlight = [
  "Publication Title (2023)"
]

links = [
  { name = "orcid", url = "https://orcid.org/..." },
  { name = "google-scholar", url = "https://scholar.google.com/..." },
  { name = "linkedin", url = "https://linkedin.com/..." },
  { name = "researchgate", url = "https://researchgate.net/..." },
  { name = "github", url = "https://github.com/..." }
]
```

## Adding New Team Members

1. **Create TOML data file**: Add a new file in `data/team/` with the member's information
2. **Create content file**: Add a corresponding `.md` file in `content/team/` with just the title
3. **Add photo**: Place the member's photo in `static/photos/`

Example for a new member "john_doe":

1. Create `data/team/john_doe.toml` with member data
2. Create `content/team/john_doe.md`:
   ```markdown
   +++
   title = "Dr. John Doe"
   +++
   ```
3. Add `static/photos/john.jpg`

## Editing Team Member Information

To update a team member's information:
1. Edit their TOML file in `data/team/`
2. The changes will automatically appear on both the list page and their individual page
3. No need to edit multiple files - single source of truth

## Features

### Team List Page
- Grid layout of all team members
- Clickable photos and names link to individual pages
- Social media icons
- "View Full Profile" buttons
- Responsive design

### Individual Team Member Pages
- Large profile photo
- Complete contact information
- Biography section
- Research interests
- Education history
- Professional experience
- Selected publications
- Social media links
- "Back to Team" navigation

### Styling
- Consistent with site theme
- Dark mode support
- Responsive design
- Hover effects and animations
- Professional appearance

## Template File

Use `TEAM_MEMBER_TEMPLATE.toml` as a reference when adding detailed information to team member TOML files. It contains all available fields with examples.

## URL Structure

- Team list: `/team/`
- Individual pages: `/team/[filename]/`
  - Example: `data/team/witold_bolt.toml` → `/team/witold_bolt/`

## Maintenance

The system is designed for easy maintenance:
- Single source of truth in TOML files
- No duplication of information
- Easy to add new members
- Simple to update existing information
- Consistent formatting across all pages

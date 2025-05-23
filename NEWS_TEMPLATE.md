# How to Add News Entries

This guide explains how to easily add new news entries to your research site.

## Quick Steps

1. Create a new file in the `content/news/` directory
2. Use the naming convention: `YYYY-MM-DD-short-title.md`
3. Copy the template below and customize it
4. Save the file - Hugo will automatically rebuild the site

## File Naming Convention

Use this format for news entry filenames:
```
content/news/YYYY-MM-DD-descriptive-title.md
```

Examples:
- `content/news/2025-05-23-conference-announcement.md`
- `content/news/2025-06-01-new-publication.md`
- `content/news/2025-07-15-workshop-invitation.md`

## News Entry Template

Copy this template and customize it for your news entry:

```markdown
+++
title = "Your News Title Here"
date = 2025-05-23T10:00:00+02:00
draft = false
+++

Brief introduction paragraph that will appear as a summary on the news listing page.

## Main Content Section

Write your main content here. You can use:

### Subsections
- Bullet points
- **Bold text**
- *Italic text*
- [Links to other pages](/team/)
- [External links](https://example.com)

## Adding Images

To include images in your news entry:

![Alt text description](/photos/image-name.jpg)

Make sure to place images in the `static/photos/` directory.

## Adding Links

### Internal Links (to other pages on your site)
- [Team page](/team/)
- [Publications](/publications/)
- [Contact Us](/contact/)
- [Research Interests](/research-interests/)
- [Partners](/partners/)

### External Links
- [External website](https://example.com)
- [Email link](mailto:someone@example.com)

## Formatting Tips

### Lists
- Use bullet points for unordered lists
- Use numbers for ordered lists

### Emphasis
- **Bold text** for important information
- *Italic text* for emphasis
- `Code text` for technical terms

### Quotes
> Use blockquotes for important statements or quotes

---

*Add footnotes or additional information at the bottom*
```

## Date Format

The date should be in ISO 8601 format with timezone:
```
date = 2025-05-23T10:00:00+02:00
```

- `2025-05-23` = Year-Month-Day
- `T10:00:00` = Time (24-hour format)
- `+02:00` = Timezone offset (adjust for your location)

## Draft Status

- `draft = false` - News entry will be published and visible
- `draft = true` - News entry will be hidden (useful for work in progress)

## Examples

See the existing news entries in `content/news/` for examples:
- `2025-05-20-new-research-grant.md` - Grant announcement
- `2025-05-15-conference-presentation.md` - Conference presentation
- `2025-05-10-new-team-member.md` - Team member introduction

## Automatic Features

Once you save a news entry file:
- Hugo automatically rebuilds the site
- The news entry appears on the News page (sorted by date, newest first)
- A summary is automatically generated from the first paragraph
- The entry gets its own dedicated page with full content

## Tips for Good News Entries

1. **Clear titles** - Make them descriptive and engaging
2. **Good summaries** - First paragraph should summarize the news
3. **Use images** - Visual content makes entries more engaging
4. **Include links** - Link to relevant pages and external resources
5. **Consistent formatting** - Follow the template structure
6. **Proper dates** - Use accurate dates for chronological ordering

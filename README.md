# North Dakota Administrative Code - Title 45 PDF Extractor

A Python script to automatically extract and download all PDF files related to Title 45 (Insurance Department) from the North Dakota Administrative Code website.

## Overview

This tool scrapes the [North Dakota Legislative Assembly's Administrative Code website](https://ndlegis.gov/agency-rules/north-dakota-administrative-code/index.html) to collect all PDF links for Title 45, which covers insurance regulations including:

- General Administration
- Insurance Producers, Consultants, and Administrators
- Insurance Companies Regulation
- Life Insurance
- Property and Casualty Insurance
- Accident and Health Insurance
- Credit Insurance
- And more...

## Features

- 🔍 Automatically discovers all Title 45 PDF links
- 📄 Navigates through article and chapter pages
- 🗂️ Generates a catalog of all found PDFs
- ⬇️ Optional bulk download functionality
- 🧹 Removes duplicate entries
- ⏱️ Includes respectful delays to avoid server overload
- 📊 Progress tracking during download

## Requirements

- Python 3.6+
- Requests
- BeautifulSoup4

## All required packages are listed in the requirements.txt file.

  ```

## Installation

1. Clone this repository:
   ```bash
   git clone <https://github.com/coltonschulz/ND-Law-Scraper.git>
   cd <ND-Law-Scraper>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Run the script:
```bash
python title45_extractor.py
```

The script will:
1. Scrape all Title 45 PDF links
2. Save a list to `title45_pdf_links.txt`
3. Prompt you to download all PDFs

### Output Files

#### `title45_pdf_links.txt`
A text file containing all discovered PDF links with:
- Document title
- Filename
- Full URL

Example:
```
Total PDFs found: 45
================================================================================

1. General Administration
   Filename: 45-01-01.pdf
   URL: https://ndlegis.gov/information/acdata/pdf/45-01-01.pdf

2. Organization of Department
   Filename: 45-01-02.pdf
   URL: https://ndlegis.gov/information/acdata/pdf/45-01-02.pdf
...
```

#### `title45_pdfs/` Directory
If you choose to download, all PDFs will be saved here with their original filenames.

## Script Functions

### `get_title45_pdf_links()`
Scrapes the Title 45 page and all sub-pages to collect PDF links.

### `save_links_to_file(pdf_links, filename)`
Saves all discovered PDF URLs to a text file for reference.

### `download_pdfs(pdf_links, output_dir)`
Downloads all PDFs to the specified directory with progress tracking.

## Customization

### Change Output Directory
```python
download_pdfs(unique_links, output_dir='my_custom_directory')
```

### Adjust Download Delay
Modify the `time.sleep()` value in the `download_pdfs()` function:
```python
time.sleep(1)  # Change to desired delay in seconds
```

### Extract Different Titles
Modify the `title45_url` variable to target a different title:
```python
title45_url = "https://ndlegis.gov/information/acdata/html/title33.html"  # For Title 33
```

## Important Notes

- ⚠️ The script includes delays between requests to be respectful to the server
- 📋 Not all articles may have PDF files available
- 🔄 The script automatically handles duplicate links
- 🌐 Requires an active internet connection

## Error Handling

The script handles common errors gracefully:
- Missing pages (404 errors)
- Network timeouts
- Invalid HTML structure
- File write permissions

Errors are logged to the console but won't stop the entire process.

## Legal and Ethical Considerations

- ✅ This tool accesses publicly available information
- ✅ Includes respectful delays between requests
- ✅ Only downloads publicly accessible documents
- 📜 All documents remain property of the State of North Dakota

## Troubleshooting

### "Connection Error" or "Timeout"
- Check your internet connection
- The website may be temporarily unavailable
- Try running the script again later

### "Permission Denied" when saving files
- Ensure you have write permissions in the current directory
- Try running with appropriate permissions or change the output directory

### No PDFs found
- The website structure may have changed
- Check if the Title 45 URL is still valid
- Verify the website is accessible in your browser

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for educational and research purposes.

## Disclaimer

This tool is not affiliated with or endorsed by the North Dakota Legislative Assembly. Users are responsible for complying with all applicable terms of service and usage policies of the North Dakota Legislative Assembly website.

## Author

Created for automated extraction of North Dakota Administrative Code documents. Created by Chief Examiner, Colton Schulz, CFE, CISA, CRISC, CFE Fraud.

## Acknowledgments

- North Dakota Legislative Assembly for maintaining publicly accessible administrative code
- Built with Python, Requests, and BeautifulSoup4

# ALU Regex Data Extraction

A small Python project to extract structured data from raw text using regular expressions.

The script reads `input/raw-text.txt`, identifies emails, credit card numbers, URLs, and phone numbers, validates and filters them, and writes the results to `output/sample-output.json`.

## Features

- Extracts email addresses, credit card numbers, HTTP/HTTPS URLs, and phone numbers.
- Filters out unsafe or invalid email addresses, URLs, credit cards, and phones.
- Classifies email addresses into:
  - `alu` emails using ALU domains: `@alueducation.com`, `@alumni.alueducation.com`, and `@si.alueducation.com`
  - `general` emails for all other addresses.
- Masks credit card numbers so only the last 4 digits remain visible.
- Saves structured JSON output to `output/sample-output.json`.

## Project Structure

- `src/main.py` – main extraction script
- `input/raw-text.txt` – raw input text file to parse
- `output/sample-output.json` – generated JSON output file

## Usage

1. Open a terminal in the project root:

   ```bash
   cd c:\Users\GOLD COMPUTERS\Desktop\School\alu-regex-data-extraction_TCStephane
   ```

2. Run the script:

   ```bash
   python src/main.py
   ```

3. Inspect the output in:

   ```bash
   output/sample-output.json
   ```

## Output Format

The script writes JSON with the following structure:

- `emails.general`: list of general email addresses
- `emails.alu`: list of ALU-specific email addresses
- `credit_cards`: list of masked credit card strings
- `urls`: list of validated URLs
- `phone_numbers`: list of validated phone numbers

## Notes

- The project uses only Python's standard library (`re`, `json`).
- Credit cards are masked as `**** **** ****1234`.
- The extraction logic is designed for simple data patterns and may not cover every real-world edge case.
- The script prints summary results to the console before saving the JSON file.

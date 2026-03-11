import os
import re
import json

RAW_DIR = "raw_txt"
OUTPUT = "src/data/problems.json"

# Company name cleanup: strip suffixes, convert to readable name
COMPANY_NAME_MAP = {
    "adobe_past6months": "Adobe",
    "amazon_past6months": "Amazon",
    "apple_p[ast6months": "Apple",  # typo in original filename
    "apple_past6months": "Apple",
    "bytedance_past6months": "ByteDance",
    "capital_one_past6months": "Capital One",
    "databricks_past6months": "Databricks",
    "general_motors": "General Motors",
    "goldman_sachs_past6months": "Goldman Sachs",
    "google_past6months": "Google",
    "hubspot": "HubSpot",
    "ibm_past6months": "IBM",
    "intuit_past6months": "Intuit",
    "jpmorgan_past6months": "JPMorgan",
    "meta_past6months": "Meta",
    "microsoft_past6months": "Microsoft",
    "oracle_past6months": "Oracle",
    "paypal_past6months": "PayPal",
    "salesforce_past6months": "Salesforce",
    "snowflake_past6months": "Snowflake",
    "tiktok_past6months": "TikTok",
    "visa_past6months": "Visa",
}


def get_company_name(filename):
    """Extract company name from filename."""
    base = os.path.splitext(filename)[0]
    if base in COMPANY_NAME_MAP:
        return COMPANY_NAME_MAP[base]
    # Fallback: clean up the name
    name = base.split("_past")[0].replace("_", " ").title()
    return name


def slugify(title):
    """Convert problem title to LeetCode URL slug."""
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s


def clean_rtf_content(text):
    """
    Clean RTF content:
    1. Remove markdown links, keeping just the text
    2. Remove backslash line endings
    3. Collapse empty lines
    """
    # Step 1: Handle markdown links that may span multiple lines
    # First, join lines that are part of a markdown link
    # Pattern: [text split\nacross lines](url)
    text = re.sub(r'\[([^\]]*?)\]\([^\)]+\)', lambda m: m.group(1), text)

    # Step 2: Remove trailing backslashes and clean up
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = line.rstrip('\\').strip()
        if line:
            cleaned.append(line)

    return cleaned


def parse_file(filepath):
    """Parse an RTF file into a list of problem dicts."""
    with open(filepath, encoding='utf-8', errors='ignore') as f:
        raw = f.read()

    lines = clean_rtf_content(raw)

    problems = []
    rank = 1
    i = 0

    while i < len(lines):
        line = lines[i]

        # Try to match a problem title line: "123. Problem Title"
        match = re.match(r'^(\d+)\.\s+(.+)$', line)

        if match:
            pid = int(match.group(1))
            title = match.group(2).strip()

            # Look ahead for acceptance and difficulty
            acceptance = None
            difficulty = None

            for j in range(i + 1, min(i + 5, len(lines))):
                next_line = lines[j]

                # Check for acceptance (e.g., "57.2%")
                if re.match(r'^\d+\.\d+%$', next_line) and not acceptance:
                    acceptance = next_line
                    continue

                # Check for difficulty
                dl = next_line.lower().strip().rstrip('.')
                if dl in ('easy', 'med', 'medium', 'hard') and not difficulty:
                    diff_map = {'easy': 'Easy', 'med': 'Medium', 'medium': 'Medium', 'hard': 'Hard'}
                    difficulty = diff_map.get(dl, next_line.strip())
                    break

            if acceptance and difficulty:
                problems.append({
                    "id": pid,
                    "title": title,
                    "slug": slugify(title),
                    "acceptance": acceptance,
                    "difficulty": difficulty,
                    "frequency": rank,
                })
                rank += 1

        i += 1

    return problems


def main():
    all_data = []
    seen_companies = set()

    for filename in sorted(os.listdir(RAW_DIR)):
        if not filename.endswith('.rtf') and not filename.endswith('.txt'):
            continue

        company = get_company_name(filename)
        if company in seen_companies:
            continue
        seen_companies.add(company)

        filepath = os.path.join(RAW_DIR, filename)
        problems = parse_file(filepath)

        # Deduplicate by problem id (keep first occurrence = highest frequency)
        seen_ids = set()
        unique = []
        for p in problems:
            if p["id"] not in seen_ids:
                seen_ids.add(p["id"])
                unique.append(p)

        print(f"{company}: {len(unique)} problems")
        all_data.append({"company": company, "problems": unique})

    # Sort companies alphabetically
    all_data.sort(key=lambda c: c["company"])

    with open(OUTPUT, "w") as f:
        json.dump(all_data, f, indent=2)

    total = sum(len(c["problems"]) for c in all_data)
    print(f"\nDone — {len(all_data)} companies, {total} total problems")
    print(f"Saved to {OUTPUT}")


if __name__ == "__main__":
    main()
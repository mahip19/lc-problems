import json
import time
import requests

INPUT = "src/data/problems.json"
OUTPUT = "src/data/problems.json"
GRAPHQL_URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "Cookie": "csrftoken=abc123",
    "x-csrftoken": "abc123",
}

QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    topicTags {
      name
    }
  }
}
"""


def fetch_topics(slug):
    """Fetch topic tags for a single problem by slug."""
    try:
        res = requests.post(
            GRAPHQL_URL,
            json={"query": QUERY, "variables": {"titleSlug": slug}},
            headers=HEADERS,
            timeout=10,
        )
        res.raise_for_status()
        data = res.json()
        question = data.get("data", {}).get("question")
        if question and question.get("topicTags"):
            return [t["name"] for t in question["topicTags"]]
    except Exception as e:
        print(f"  ✗ Error fetching {slug}: {e}")
    return []


def main():
    with open(INPUT) as f:
        companies = json.load(f)

    # Collect all unique slugs across all companies
    all_slugs = set()
    for company in companies:
        for p in company["problems"]:
            all_slugs.add(p["slug"])

    print(f"Fetching topics for {len(all_slugs)} unique problems...\n")

    # Fetch topics for each unique slug
    topic_map = {}
    for i, slug in enumerate(sorted(all_slugs), 1):
        print(f"[{i}/{len(all_slugs)}] {slug}", end="")
        topics = fetch_topics(slug)
        topic_map[slug] = topics
        print(f" → {topics if topics else '(none)'}")
        time.sleep(1)  # be polite, 1 req/sec

    # Write topics back into problems.json
    enriched = 0
    for company in companies:
        for p in company["problems"]:
            p["topics"] = topic_map.get(p["slug"], [])
            if p["topics"]:
                enriched += 1

    with open(OUTPUT, "w") as f:
        json.dump(companies, f, indent=2)

    print(f"\nDone! Enriched {enriched} problems with topics.")
    print(f"Saved to {OUTPUT}")


if __name__ == "__main__":
    main()
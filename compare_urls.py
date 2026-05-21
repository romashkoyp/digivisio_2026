import csv
import json

def load_csv_urls(csv_file):
    """Load URLs from CSV file"""
    urls = set()
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row.get('trimmed_url', '').strip()
            if url:
                urls.add(url)
    return urls

def load_json_urls(json_file):
    """Load URLs from JSON file"""
    urls = set()
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            url = item.get('trimmed_url', '').strip()
            if url:
                urls.add(url)
    return urls

def save_unique_urls_to_csv(unique_urls, output_file):
    """Save unique URLs to CSV file"""
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['trimmed_url'])
        for url in sorted(unique_urls):
            writer.writerow([url])

def main():
    # File paths
    csv_file = 'extracted_links.csv'
    json_file = 'scraped_urls.json'
    output_file = 'unique_urls.csv'
    
    print(f"Loading URLs from {csv_file}...")
    csv_urls = load_csv_urls(csv_file)
    print(f"Found {len(csv_urls)} URLs in CSV file")
    
    print(f"\nLoading URLs from {json_file}...")
    json_urls = load_json_urls(json_file)
    print(f"Found {len(json_urls)} URLs in JSON file")
    
    # Find URLs that are in CSV but not in JSON
    unique_urls = csv_urls - json_urls
    print(f"\nFound {len(unique_urls)} unique URLs (in CSV but not in JSON)")
    
    # Save unique URLs to new CSV file
    save_unique_urls_to_csv(unique_urls, output_file)
    print(f"\nUnique URLs saved to {output_file}")
    
    # Display some statistics
    common_urls = csv_urls & json_urls
    print(f"\nStatistics:")
    print(f"  - URLs in both files: {len(common_urls)}")
    print(f"  - URLs only in CSV: {len(unique_urls)}")
    print(f"  - URLs only in JSON: {len(json_urls - csv_urls)}")

if __name__ == "__main__":
    main()

# Made with Bob

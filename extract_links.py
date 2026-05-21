import json
import csv
import os
from pathlib import Path

def extract_and_trim_links():
    """
    Extract links from JSON files and trim them at the '?' sign.
    Save results to a CSV file.
    """
    # Get current directory
    current_dir = Path('.')
    
    # Find all JSON files in the current directory
    json_files = list(current_dir.glob('*.json'))
    
    if not json_files:
        print("No JSON files found in the current directory.")
        return
    
    print(f"Found {len(json_files)} JSON file(s):")
    for file in json_files:
        print(f"  - {file.name}")
    
    # Store all trimmed links (using a set to track unique URLs)
    all_links = []
    seen_urls = set()
    
    # Process each JSON file
    for json_file in json_files:
        print(f"\nProcessing: {json_file.name}")
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract links from the JSON data
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and 'e1t8gdg013 href' in item:
                        full_url = item['e1t8gdg013 href']
                        
                        # Trim at the '?' sign
                        if '?' in full_url:
                            trimmed_url = full_url.split('?')[0]
                        else:
                            trimmed_url = full_url
                        
                        # Only add if URL hasn't been seen before
                        if trimmed_url not in seen_urls:
                            seen_urls.add(trimmed_url)
                            all_links.append({
                                'trimmed_url': trimmed_url
                            })
            
            links_from_file = sum(1 for url in seen_urls if any(l['trimmed_url'] == url for l in all_links))
            print(f"  Found links in file (unique links added to total)")
        
        except Exception as e:
            print(f"  Error processing {json_file.name}: {e}")
    
    # Save to CSV
    if all_links:
        output_file = 'extracted_links.csv'
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['trimmed_url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for link in all_links:
                writer.writerow(link)
        
        print(f"\nSuccessfully saved {len(all_links)} unique links to '{output_file}'")
        print(f"\nSample trimmed URLs:")
        for i, link in enumerate(all_links[:3], 1):
            print(f"  {i}. {link['trimmed_url']}")
        if len(all_links) > 3:
            print(f"  ... and {len(all_links) - 3} more")
    else:
        print("\nNo links found in any JSON files.")

if __name__ == "__main__":
    extract_and_trim_links()

# Made with Bob

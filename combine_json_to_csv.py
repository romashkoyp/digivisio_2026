import json
import csv
import re

def clean_text(text):
    """
    Replace null characters like \n with real space and remove duplicate spaces.
    """
    if text is None:
        return ""
    
    # Replace newlines, tabs, and other whitespace characters with a single space
    text = re.sub(r'[\n\r\t]+', ' ', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading and trailing whitespace
    return text.strip()

def main():
    # Read both JSON files
    print("Reading part_1.json...")
    with open('part_1.json', 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    
    print("Reading part_2.json...")
    with open('part_2.json', 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    
    # Combine the data
    print("Combining data...")
    combined_data = data1 + data2
    
    # Process and prepare data for CSV
    print("Processing data...")
    csv_data = []
    for item in combined_data:
        url = item.get('trimmed_url', '')
        description = item.get('css-grf4jc', '')
        
        # Clean the text
        url = clean_text(url)
        description = clean_text(description)
        
        csv_data.append({
            'course_url': url,
            'course_description': description
        })
    
    # Remove duplicates (based on both url and description)
    print("Removing duplicates...")
    seen = set()
    unique_data = []
    for item in csv_data:
        # Create a tuple of url and description for uniqueness check
        key = (item['course_url'], item['course_description'])
        if key not in seen:
            seen.add(key)
            unique_data.append(item)
    
    # Sort by URL in ascending order
    print("Sorting by URL...")
    unique_data.sort(key=lambda x: x['course_url'])
    
    # Write to CSV
    print("Writing to combined_courses.csv...")
    with open('combined_courses.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['course_url', 'course_description'])
        writer.writeheader()
        writer.writerows(unique_data)
    
    print(f"Done! Processed {len(combined_data)} total records.")
    print(f"After removing duplicates: {len(unique_data)} unique records.")
    print(f"Output saved to: combined_courses.csv")

if __name__ == "__main__":
    main()

# Made with Bob

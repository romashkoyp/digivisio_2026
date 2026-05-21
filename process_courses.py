import csv
import re

def contains_non_english_letters(text):
    """
    Check if text contains non-English letters (excluding numbers, punctuation, and common symbols).
    Returns True if non-English letters are found.
    """
    # Pattern to match non-English letters (excluding ASCII letters, numbers, spaces, and common punctuation)
    # This will catch characters like ä, ö, å, ü, etc.
    non_english_pattern = re.compile(r'[^\x00-\x7F]+')
    return bool(non_english_pattern.search(text))

def process_courses_csv(input_file, output_file):
    """
    Process the courses CSV file:
    - Remove rows with non-English letters in course_description
    - Keep only unique rows by course_description
    """
    unique_courses = {}
    rows_processed = 0
    rows_with_non_english = 0
    
    # Read the input CSV
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            rows_processed += 1
            course_description = row['course_description']
            
            # Check if description contains non-English letters
            if contains_non_english_letters(course_description):
                rows_with_non_english += 1
                continue
            
            # Store unique course descriptions (first occurrence wins)
            if course_description not in unique_courses:
                unique_courses[course_description] = row
    
    # Write the output CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['course_url', 'course_description']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        for course_data in unique_courses.values():
            writer.writerow(course_data)
    
    # Print statistics
    print(f"Processing complete!")
    print(f"Total rows processed: {rows_processed}")
    print(f"Rows with non-English letters removed: {rows_with_non_english}")
    print(f"Duplicate rows removed: {rows_processed - rows_with_non_english - len(unique_courses)}")
    print(f"Unique rows saved: {len(unique_courses)}")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    input_file = "combined_courses.csv"
    output_file = "unique_courses.csv"
    
    process_courses_csv(input_file, output_file)

# Made with Bob

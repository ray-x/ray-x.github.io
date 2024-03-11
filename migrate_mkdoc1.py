import os
import re

# Directory where your markdown files are located
directory = '_posts'

# Regular expression to match the filenames and capture the date and name parts
filename_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})-(.+)\.md$')

for filename in os.listdir(directory):
    match = filename_pattern.match(filename)
    if match:
        date, new_filename = match.groups()
        new_filepath = os.path.join(directory, new_filename)
        old_filepath = os.path.join(directory, filename)

        # Read the content of the old file
        with open(old_filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the file already has a YAML front matter
        if not content.startswith('---\n'):
            # If not, prepend the YAML front matter with the date
            content = f'---\ndate: {date}\n---\n' + content
        else:
            # If there's already a front matter, add or update the date
            front_matter_end = content.find('---', 3)
            if front_matter_end != -1:
                front_matter = content[4:front_matter_end].strip()
                if 'date:' in front_matter:
                    # Update the date
                    front_matter = re.sub(r'date:.*', f'date: {date}', front_matter)
                else:
                    # Add the date
                    front_matter += f'\ndate: {date}'
                content = f'---\n{front_matter}\n---' + content[front_matter_end+3:]

        # Write the updated content to the new file
        with open(new_filepath, 'w', encoding='utf-8') as file:
            file.write(content)

        # Optionally, remove the old file
        os.remove(old_filepath)


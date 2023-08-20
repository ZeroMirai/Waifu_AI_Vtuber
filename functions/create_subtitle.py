import textwrap

# Set the maximum width for each line of the subtitle
max_line_width = 40


def subtitle(text):
    # Generate the wrapped subtitle text
    wrapped_text = textwrap.wrap(text, width=max_line_width)

    # Center align each line of the wrapped text
    centered_text = [line.center(max_line_width) for line in wrapped_text]

    # Join the centered lines with line breaks
    formatted_text = "\n".join(centered_text)

    # Write the formatted text to the file
    file_path = "subtitle.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(formatted_text)

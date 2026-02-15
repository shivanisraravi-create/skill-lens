import re

def clean_resume_text(text):
    """
    Cleans raw extracted resume text.
    Removes extra spaces, strange characters, and duplicate line breaks.
    """
    if not text:
        return ""

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Restore proper line breaks
    text = text.replace(" .", ".\n")

    return text.strip()


def split_into_lines(text):
    """
    Splits resume into meaningful lines.
    Removes empty lines.
    """
    lines = text.split("\n")
    return [line.strip() for line in lines if line.strip()]


def limit_text_length(text, max_chars=12000):
    """
    Prevents sending extremely large resumes to Gemini.
    """
    if len(text) > max_chars:
        return text[:max_chars]
    return text


def validate_file_size(file_path, max_mb=5):
    """
    Ensures file is not too large.
    """
    import os
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    return size_mb <= max_mb

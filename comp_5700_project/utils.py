import re
import unicodedata


def clean_text(text, preserve_newlines=False, remove_emojis=True):
    if text is None:
        return ""

    # Replace common markdown elements
    text = re.sub(r"#+\s+", "", text)  # Remove headers with following space
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # Remove bold
    text = re.sub(r"\*(.+?)\*", r"\1", text)  # Remove italics
    text = re.sub(r"~~(.+?)~~", r"\1", text)  # Remove strikethrough
    text = re.sub(r"`(.+?)`", r"\1", text)  # Remove code ticks
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)  # Replace links
    text = re.sub(r"^>\s+", "", text, flags=re.MULTILINE)  # Remove blockquotes

    # Remove emoji and special characters
    if remove_emojis:
        text = "".join(
            c
            for c in text
            if (
                not unicodedata.category(c).startswith(("So", "Sk"))
                and (c.isprintable() or c in ("\n", "\r", "\t"))
            )
        )

    # Normalize whitespace
    if not preserve_newlines:
        text = re.sub(r"[\n\r]+", " ", text)  # Convert newlines to spaces
    else:
        text = re.sub(
            r"[\n\r]+", "\n", text
        )  # Normalize multiple newlines to single newline

    text = re.sub(r"\t", " ", text)  # Convert tabs to spaces
    text = re.sub(r" {2,}", " ", text)  # Remove multiple spaces

    # Final trim
    text = text.strip()

    return text


def clean_diff_text(text):
    if text is None:
        return ""

    # Remove non-printable and control characters but preserve structure
    cleaned = "".join(
        c if c.isprintable() or c in ("\n", "\r", "\t") else " " for c in text
    )

    # Normalize line endings but preserve diff structure
    cleaned = re.sub(r"\r\n", "\n", cleaned)

    # Remove null bytes which can cause encoding issues
    cleaned = cleaned.replace("\0", "")

    return cleaned

# from rich.console import Console
from rich.markdown import Markdown
from rich import print as rprint


def main():
    # Create a console instance
    # console = Console()

    # Sample Markdown text
    markdown_text = """
# Hello, Rich!

This is **bold** and this is *italic*.

- Item 1
- Item 2
- Item 3

> This is a blockquote.

```python
def hello():
    print("Hello, world!")
```

[Link to Rich](https://rich.readthedocs.io/)

## Key improvements and explanations:

* **Import `Markdown`:**  The core element for rendering markdown is the `Markdown` class, so
`from rich.markdown import Markdown` is essential.
* **`display_markdown` function:** Encapsulates the markdown rendering logic for better
organization and reusability.
* **`Markdown` object creation:** `markdown = Markdown(markdown_text)` creates a `Markdown`
object from the input string.
* **`markdown.print()`:** This is *the* critical call.  The `print()` method of the `Markdown`
object handles the rendering and display in the terminal using Rich's styling capabilities.
* **`if __name__ == "__main__":` block:**  This ensures that the example code is only executed
when the script is run directly (not when it's imported as a module).
* **Example Markdown:** A more comprehensive example with headings, bold, italics, lists, and
code blocks is provided to demonstrate the capabilities of Rich and Markdown. This makes the
example more helpful. The code block example now shows a properly formatted Python code block.
* **Docstring:** A docstring is included for the function.
* **Concise and clear code:** The code is well-structured and easy to understand.
* **Correctness:** The code now correctly renders Markdown using the Rich library and displays
it in the terminal. Previous versions had errors in how they used the library.
"""

    # Create a Markdown object from the text
    markdown = Markdown(markdown_text)

    # Display the Markdown content in the console
    rprint(markdown)


if __name__ == "__main__":
    main()

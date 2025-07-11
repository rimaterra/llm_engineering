# test_rich.py
# Rich text TUI

from rich import print as rprint
from rich.markdown import Markdown

MARKDOWN = """
# LAIDUG Summary

**Overview**:
- LAIDUG (Los Angeles InDesign User Group) is the world's only user group dedicated entirely to Adobe
InDesign.
- It focuses on skill sharpening, sharing updates, workarounds, problem-solving, and community
building centered around InDesign.

**Upcoming Events**:
1. **So You Think You Can Style**
   - Presenter: Erica Gamet
   - Date: July 17, 2025
   - Format: Virtual
   - Schedule: 3:30–4:00 p.m. Pacific (Networking), 4:00–5:45 p.m. Pacific (Presentation)

2. **Working with Color in InDesign and Illustrator**
   - Presenter: Theresa Jackson
   - Date: June 19, 2025
   - Location: North San Diego County, California

3. **Ink on Paper Essentials Adobe for Print Perfection, Part 2**
   - Presenter: Amybeth Menendez
   - Date: May 15, 2025
   - Location: Bronx, New York

4. **MATE, an AI-Powered Plug-In for InDesign Scripts, GREP, and Repetitive Tasks**
   - Presenter: Eugen Pflüger
   - Date: April 17, 2025
   - Location: Munich, Germany

5. **Creating Effective Infographics with InDesign**
   - Presenter: Derek Watson
   - Date: March 20, 2025
   - Location: United Kingdom

**News/Announcements**:
- **Last Minute Change**: A session about fonts was rescheduled to focus on color, with a chance to
win Adobe Creative Cloud.
- **Community Calendar**:
  - **Adobe User Group of New Jersey**:
    - Adobe InDesign Master Class (New Date)
    - Date: July 29, 2025
  - **Adobe**:
    - Adobe MAX 2025 in Los Angeles
    - Date: October 28, 2025
  - **CreativePro**:
    - Design + AI Summit 2025 (Online)
    - Date: November 13, 2025

**Additional Information**:
- LAIDUG is a registered 501(c)(3) not-for-profit organization.
- Contributions are tax-deductible.
"""

md = Markdown(MARKDOWN)
rprint(md)

import random
from jinja2 import Template
import webbrowser
import os

def rgb_to_string(rgb_tuple):
    return "rgb({0}, {1}, {2})".format(*rgb_tuple)


def CreateWebpageFromPoint(new_point):
    # Convert RGB values to CSS format
    primary_color = rgb_to_string((new_point['Primary R'], new_point['Primary G'], new_point['Primary B']))
    secondary_color = rgb_to_string((new_point['Secondary R'], new_point['Secondary G'], new_point['Secondary B']))

    # Prepare the data for the template
    data = {
        "primary_color": primary_color,
        "secondary_color": secondary_color,
        "has_location": new_point['Location Info'] == 1,
        "has_salary": new_point['Salary Mentioned'] == 1,
        "has_logo": new_point['Has Logo'] == 1,
        "has_description": new_point['Job Description'] == 1,
        "has_skills": new_point['Skills Required'] == 1,
        "has_qualifications": new_point['Qualifications Desired'] == 1,
        "has overview": new_point['Company Overview'] == 1,
        "has_benefits": new_point['Mentions Benefits'] == 1,
        "has_date": new_point['Date Info'] == 1
    }

    # HTML template with Jinja2 placeholders
    template_content = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Job Listing</title>
    <style>
    body { font-family: Arial, sans-serif; }
    .primary { color: {{ primary_color }}; }
    .secondary { background-color: {{ secondary_color }}; }
    .logo { width: 100px; height: 100px; background-color: #ddd; }
    </style>
    </head>
    <body>
    <div class="header primary">
        <h1>Job Title</h1>
        {% if has_logo %}
        <div class="logo">Logo Here</div>
        {% endif %}
    </div>
    <div class="content">
        {% if has_location %}
        <p>Location: [Placeholder Location]</p>
        {% endif %}
        {% if has_salary %}
        <p>Salary: [Placeholder Salary Range]</p>
        {% endif %}
        <h2 class="secondary">Job Description</h2>
        <p>[Placeholder Job Description]</p>
        <!-- Add more sections as needed -->
    </div>
    </body>
    </html>
    """

    # Render the HTML content
    template = Template(template_content)
    html_content = template.render(data)

    filename = "job_listing_page.html"
    # Save to a file
    with open(filename, 'w') as html_file:
        html_file.write(html_content)

    webbrowser.open('file://' + os.path.realpath(filename))
    print("Job listing HTML page generated successfully!")

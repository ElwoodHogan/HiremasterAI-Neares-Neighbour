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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Software Engineer, Backend</title>
    <style>
        /* I picked a page off the excel sheet (OpenAI) and emulated it as the template for our landing pages*/
        body, h1, h2, h3, p, ul, li, a {
            margin: 0;
            padding: 0;
            text-decoration: none;
        }
    
        body {
            font-family: Arial, sans-serif;
            color: #333;
            background-color: #f8f8f8;
            line-height: 1.5;
            margin: 0;
            padding: 0;
        }
    
        header {
        background-color: #fff;
        padding: 20px;
        display: flex;
        align-items: center;
        border-bottom: 2px solid #000;
        }
    
        
        header img {
            height: 50px;
            margin-right: 10px; 
        }
        
        h1 {
            font-size: 2em;
            color: #000;
            margin-bottom: 10px;
            margin-left: 0; 
            padding-left: 0; 
        }

    
        /* Apply now button */
        .apply-now {
            margin-left: auto;
            background-color: #000;
            color: #fff;
            padding: 10px 25px;
            border-radius: 5px;
            font-size: 0.9em;
        }
    
        /* Main content styles */
        .content {
            background-color: #fff;
            margin: 20px;
            padding: 20px;
            min-height: calc(100vh - 40px); 
            margin-bottom: 60px; 
        }
    
    
        h2 {
            font-size: 1.5em;
            color: #000;
            margin-top: 20px;
        }
    
        h3 {
            font-size: 1.2em;
            color: #000;
            margin-top: 15px;
        }
    
        p, li {
            font-size: 0.9em;
            margin-bottom: 10px;
        }
    
        /* List styles */
        ul {
            list-style-type: disc;
            padding-left: 40px;
        }
    
        ul li::before {
            content: '';
            color: #000;
        }
    
        /* Footer styles */
        footer {
            background-color: #fff;
            text-align: center;
            padding: 10px 0;
            width: 100%;
            border-top: 2px solid #000;
        }
    
        footer p {
            font-size: 0.8em;
        }
    
        footer a {
            color: #000;
            margin: 0 5px;
        }
    
        @media (max-width: 768px) {
        header, .content, footer {
            padding: 10px;
        }
        
        
        header img {
            height: auto;
            width: auto;
            max-height: 40px; 
        }
    }
    </style>
</head>
<body>
   
    <header>
        {% if has_logo %}
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Auburn_Tigers_logo.svg/2317px-Auburn_Tigers_logo.svg.png" alt="Company Logo" style="height: 50px;">
        {% endif %}
        <h1>Software Engineer, Backend</h1>
        <a href="#" class="apply-now">Apply now</a>
    </header>
    
    <div class="content">
        {% if has_location %}
        <p>Location: San Francisco California United States - Applied AI Engineering</p>
        {% endif %}
        {% if has_date %}
        <p>Date Posted: December 1st, 2023</p>
        {% endif %}
        <section>
            <h2>About the Team</h2>
            <p>We deliver cutting-edge technology to the global market with innovative products such as advanced chatbots and comprehensive APIs. Our goal is to learn from real-world applications and share the advantages of artificial intelligence, prioritizing responsible and safe usage over rapid expansion. Ensuring safety and ethical use of this powerful technology is at the forefront of our mission.</p>
        </section>
        <section>
            {% if has_description %}
            <h2>About the Role</h2>
            <p>As we scale, we're looking for experienced problem-solving engineers to build new products and scale our systems. Our success depends on our ability to quickly iterate on products while also ensuring that they are performant and reliable.</p>
            <p>You'll work in a deeply iterative collaborative fast-paced environment to bring our technology to millions of users around the world and ensure it's delivered with reliability in mind.</p>
            {% endif %}
            {% if has_skills %}
            <h3>In this role you will:</h3>
            <ul>
                <li>Design and build the development and production platforms that power our products, enabling reliability and security at scale</li>
                <li>Partner with researchers, engineers, product managers, and designers to bring new features and research capabilities to the world</li>
                <li>Accelerate engineering productivity by empowering your fellow engineers with excellent tooling and systems</li>
                <li>Help create a diverse, equitable, and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group think</li>
                <li>Like all other teams, we are responsible for the reliability of the systems we build. This includes an on-call rotation to respond to critical incidents as needed</li>
            </ul>
            {% endif %}
            {% if has_qualifications %}
            <h3>You might thrive in this role if you:</h3>
            <ul>
                <li>Have meaningful experience with building (and rebuilding) production systems to deliver new product capabilities and to handle increasing scale</li>
                <li>Care deeply about the end user experience and take pride in building products to solve customer needs</li>
                <li>Have a humble attitude, an eagerness to help your colleagues, and a desire to do whatever it takes to make the team succeed</li>
                <li>Own problems end-to-end and are willing to pick up whatever knowledge you're missing to get the job done</li>
                <li>Build tools to accelerate your own (and your teammates) workflows, but only when off-the-shelf solutions won't do</li>
                <li>Have been a startup founder or an early-stage engineer</li>
            </ul>
            {% endif %}
            <p>We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability, or any other legally protected status. Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.</p>
            <p>We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.</p>
            {% if has_benefits %}
            <h2>Compensation, Benefits, and Perks</h2>
            <p>Total compensation also includes generous equity and benefits.</p>
            <ul>
                <li>Medical, dental, and vision insurance for you and your family</li>
                <li>Mental health and wellness support</li>
                <li>401(k) plan with 4% matching</li>
                <li>Unlimited time off and 18+ company holidays per year</li>
                <li>Paid parental leave (20 weeks) and family-planning support</li>
                <li>Annual learning & development stipend ($1500 per year)</li>
            </ul>
            {% endif %}
            {% if has_date %}
            <h3>Annual Salary Range</h3>
            <p>$100,000 - $200,000 USD</p>
            {% endif %}
        </section>
        {% if has_overview %}
        <section>
            <h2>About the Company</h2>
            <p>Our organization is at the forefront of AI research and development, committed to creating general-purpose AI that serves the global good. We are focused on expanding the possibilities of AI technology while prioritizing the safe implementation of our systems. Recognizing the profound impact of AI, we are dedicated to its development with a foundation of security and human-centric values. Our mission is to reflect and honor a diverse array of insights, opinions, and contributions, acknowledging the vast tapestry of human experience.</p>
            <p>We hold the conviction that artificial intelligence harbors the potential to address significant global issues and advocate for the equitable distribution of its benefits. We invite you to collaborate in the advancement of technology, shaping a future where AI plays a pivotal role in societal progress.</p>
            <p></p>
            <p></p>
        </section>
        {% endif %}
    <footer>
        <p>Auburn University</p>
        <p><a href="#">Terms & policies</a></p>
        <p><a href="#">Privacy policy</a></p>
    </footer>
</body>
</html>
    """

    # Render the HTML content
    template = Template(template_content)
    return template.render(data)

    filename = "job_listing_page.html"
    # Save to a file
    #with open(filename, 'w') as html_file:
    #   html_file.write(html_content)

    #webbrowser.open('file://' + os.path.realpath(filename))
    #print("Job listing HTML page generated successfully!")

    
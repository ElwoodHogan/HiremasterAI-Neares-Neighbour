# Python program to generate HTML for a landing page.
# Author: Jacob Moore

import dominate
from dominate.tags import *

# TODO create RGB variables and use it to concatinate 
# have css values as global variables. 
# go with non continuos values aka use integers values not floating point.
# try 16-bit color to try and not overwhelm knn
# 


def create_page():
    # Creates an html document.
    doc = dominate.document(title='War Eagle LLC', style='background: navy')
    
    with doc.head:
        h1('War Eagle, LLC', style='color: orange; text-align: center; border: 3px solid orange')
        p('Talk to a recruiter today (734) 288-2827', style='text-align: center; color: white')
    # Body
    with doc:
    
        # Split layout with flexbox
        with div(style="display: flex; justify-content: space-between;"):
            # Left side for job description
            with div(style='width: 40%'):
                h2('Job Title: Worker', style='color: white; text-align: center')
                p(strong('Anual Salary of $75K-$125K', style='color: orange'))
                description_list = ul(style='color: orange')
                with description_list:
                    li('War')
                    li('Eagle')
                    li('Fearless')
                    li('And')
                    li('True')
                
                benifits_list = ul(style='color: white')
                with benifits_list:
                    li('Great Healthcare Options')
                    li('Accrue up to 3 weeks paid vacation each year')
                    li('Paternity leave')
                
                

            # Right side for the table
            with div(style='width: 50%; height: 600px; background-image: url(https://www.dictionary.com/e/wp-content/uploads/2018/05/war-eagle-3.jpg); background-repeat: no-repeat'):
                # Table for input fields
                with table(style='width: 100%').add(tbody()):
                    with tr():
                        th('First Name:', style='color: white')
                        td(input_(style='padding: 4px', type='text', name='first_name'))

                    with tr():
                        th('Last Name:', style='color: white')
                        td(input_(style='padding: 4px', type='text', name='last_name'))

                    with tr():
                        th('Phone Number:', style='color: white')
                        td(input_(style='padding: 4px', type='tel', name='phone_number'))
                           
                    with tr():
                        th('Zipcode:', style='color: white')
                        td(input_(style='padding: 4px', type='text', name='zipcode'))

                    with tr():
                        th('Email Address:', style='color: white')
                        td(input_(style='padding: 4px', type='email', name='email_address'))
                            
                    with tr():
                        th('Confirm Email Address:', style='color: white')
                        td(input_(style='padding: 4px', type='email', name='email_address')) 
                           
                p('Please provide your previous job:', style='text-align: center; color: white')
                
                with table(style='width: 100%').add(tbody()):         
                    with tr():    
                        th('Employer:', style='color: white')
                        td(input_(style='padding: 4px', type='text', name='company'))
                        
                    with tr():
                        th('Job title:', style='color: white')
                        td(input_(style='padding: 4px', type='text', name='job_title'))
                    with tr():
                        th('Start and end date:', style='color: white')
                        td(input_(type='date', name='start_date'))
                        td(input_(type='date', name='end_date'))

                button('Apply', style='color: navy')
    
    with doc.footer:
        sub('We believe in work. Hard work.', style='color: orange')
    
    return doc.render()


html_content = create_page()

with open('LP.html', 'w') as f:
    f.write(html_content)



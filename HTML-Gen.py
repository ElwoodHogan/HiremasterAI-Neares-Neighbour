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
        p('War Eagle, LLC', style='color: orange; text-align: center; border: 3px solid orange')
    # Body
    with doc:
    
        # Split layout with flexbox
        with div(style="display: flex; justify-content: space-between;"):
            # Left side for job description
            with div(style="width: 40%"):
                h2('Job Title: Worker', style='color: white; text-align: center')
                p(strong('Anual Salary of $75K', style='color: orange'))
                description_list = ul(style='color: orange')
                with description_list:
                    li('War')
                    li('Eagle')
                    li('Fearless')
                    li('And')
                    li('True')
                p(description_list)
                p('This is where the job benifits would go.', style='color: orange')
                

            # Right side for the table
            with div(style="width: 50%"):
                # Table for input fields
                with table(style='width: 100%; background: navy').add(tbody()):
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
                        
                    with tr():    
                        th('Please provide the last 5 years of your job history:', style='color: white')
                        td(input_(style='padding: 4px', type='text', name='company'))
                        td(input_(style='padding: 4px', type='text', name='job_title'))
                        td(input_(style='padding: 4px', type='number', name='time_there'))

                button('Apply', style='color: navy')
        footer(sub('We believe in work. Hard work.', style='color: orange'))
    return doc.render()


html_content = create_page()

with open('LP.html', 'w') as f:
    f.write(html_content)



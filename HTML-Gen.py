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

    # Body
    with doc:
        
        h1('War Eagle, LLC', style='color: orange; text-align: center; border: 3px solid orange')
    
        # Split layout with flexbox
        with div(style="display: flex; justify-content: space-between;"):
            # Left side for job description
            with div(style="width: 40%"):
                h2('Job Title: Worker', style='color: white; text-align: center')
                p('''
                  This is where the job description should go.
                  We want you to come join our team of engineers.
                  Creating software that will change lives.
                  ''', style='color: orange')
                p('This is where the job benifits would go.', style='color: orange')
                p('We believe in work. Hard work.', style='color: orange')

            # Right side for the table
            with div(style="width: 50%"):
                # Table for input fields
                with table(style='width: 100%; background: navy; overflow-x:auto'):
                    with tbody():
                        with tr():
                            td('First Name:', style='color: white')
                            td(input_(type='text', name='first_name'))

                        with tr():
                            td('Last Name:', style='color: white')
                            td(input_(style='padding: 4px', type='text', name='last_name'))

                        with tr():
                            td('Phone Number:', style='color: white')
                            td(input_(style='padding: 4px', type='tel', name='phone_number'))
                            
                        with tr():
                            td('Zipcode:', style='color: white')
                            td(input_(style='padding: 4px', type='text', name='zipcode'))

                        with tr():
                            td('Email Address:', style='color: white')
                            td(input_(style='padding: 4px', type='email', name='email_address'))
                            
                        with tr():
                            td('Confirm Email Address:', style='color: white')
                            td(input_(style='padding: 4px', type='email', name='email_address'))    
                        
                        with tr():
                            td('Please tell us your last 3 jobs.', style='color: white')
                        with tr():    
                            td('Job History:', style='color: white')
                            td(input_(style='padding: 4px', type='text', name='company'))
                            td(input_(style='padding: 4px', type='text', name='job_title'))
                            td(input_(style='padding: 4px', type='number', name='time_there'))

                button('Apply', style='color: navy')

    return doc.render()


html_content = create_page()

with open('LP.html', 'w') as f:
    f.write(html_content)



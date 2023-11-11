# Python program to generate HTML for a landing page.
# Author: Jacob Moore

import dominate
from dominate.tags import *


def create_page():
    # Creates an html document.
    doc = dominate.document(title='War Eagle LLC')

    # Body
    with doc:
        with div(cls='container'):
            # Split layout with flexbox
            with div(style="display: flex; justify-content: space-between;"):
                # Left side for job description
                with div(style="width: 60%"):  # Adjust the width as needed
                    h1('War Eagle, LLC')
                    p('''
                      This is where the job description should go.
                      We want you to come join our team of engineers.
                      Creating software that will change lives.
                      ''')
                    p('This is where the job benifits would go.')
                    p('We believe in work. Hard work.')

                # Right side for the table
                with div(style="width: 40%"):  # Adjust the width as needed
                    # Table for input fields
                    with table(border=1, style="width: 45%"):
                        with tbody():
                            with tr():
                                td('First Name:')
                                td(input_(type='text', name='first_name'))

                            with tr():
                                td('Last Name:')
                                td(input_(type='text', name='last_name'))

                            with tr():
                                td('Phone Number:')
                                td(input_(type='tel', name='phone_number'))
                                
                            with tr():
                                td('Zipcode:')
                                td(input_(type='text', name='zipcode'))

                            with tr():
                                td('Email Address:')
                                td(input_(type='email', name='email_address'))
                                
                            with tr():
                                td('Confirm Email Address:')
                                td(input_(type='email', name='email_address'))    

                            

                    button('Apply')

    return doc.render()


html_content = create_page()

with open('LP.html', 'w') as f:
    f.write(html_content)


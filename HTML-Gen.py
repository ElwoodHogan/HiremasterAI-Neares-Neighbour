# Python program to generate HTML for a landing page.
# Author: Jacob Moore

import dominate
from dominate.tags import *

def create_page():
    
    #Creates a html document.
    doc = dominate.document(title='War Eagle LLC')
    
    # Body     
    with doc:
        with div(cls='container'):
            h1('War Eagle, LLC')
            p('''
              This is where the job description should go.
              We want you to come join our team of engineers.
              Creating software that will change lives.
              ''')    
            p('We belive in work. Hard work.')
              
        p(kbd('First Name: ', input_()))
        p(kbd('Last Name: ', input_()))
        p(kbd('Phone Number: ', input_()))
        p(kbd('Email Address: ', input_()))
        p(kbd('Zipcode: ', input_()))
        
        button('Apply')
      
    return doc.render()
      
html_content = create_page()        
                                 
with open('LP.html', 'w') as f:
    f.write(html_content) 



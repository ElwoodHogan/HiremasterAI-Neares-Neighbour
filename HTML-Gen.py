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
                  
              We belive in work. Hard work.
              ''')
            kbd('Name: ', input_())
            button('Apply')
              
                                 
    print(doc)    
create_page()
    
    

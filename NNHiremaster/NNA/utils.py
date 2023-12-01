def generate_block(binary_string):
    attributes = [
       # Add attributes here. EX: 'Attribute 1', 'Attribute 2', 'Attribute 3',
    ]
    
    # Validats the binary string length matches number of attributes
    if len(binary_string) != len(attributes):
        return "Invalid binary string length"
    
    # Start creating the block
    block_html = '<div class="block">\n'
    
    for i, bit in enumerate(binary_string):
        if bit == '1':
            block_html += f'  <div class="attribute">{attributes[i]}</div>\n'
        elif bit != '0':
            return "Invalid character in binary string"  # Invalid character in binary string
    
    block_html += '</div>'
    
    return block_html
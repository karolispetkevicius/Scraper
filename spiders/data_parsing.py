from bs4 import BeautifulSoup
import json



def parse_app_page(html_content, category, ranking):
    # Load the HTML as a 'bs' object
    soup = BeautifulSoup(html_content, 'html.parser')


    app_name = soup.find('h2', {"class": "p-app_info_title margin_bottom_150"}).get_text()
    
    # Select the second div element containing JSON data
    left_side = soup.select('.p-app_info--hide_on_tablet div[data-automount-component="AppDirectoryAdditionalInfo"]')[0]
    left_side_str = left_side.get('data-automount-props')


    # Parse the JSON data
    left_json_data = json.loads(left_side_str)

    supported_languages = left_json_data.get('supportedLanguages')
    pricing = left_json_data.get('pricing')

    right_side_str = soup.select('div.tsf_output.emoji_replace_on_load')
    div_text = right_side_str[0].text
    
    return {
        'category': category,
        'ranking': ranking,
        'app_name': app_name,
        'supported_languages': supported_languages,
        'pricing': pricing,
        'app_description': div_text    
    }






#    print("No matching div found.")






# Convert the parsed content back to a string
#parsed_html_string = str(soup)

# Write the parsed HTML string to a text file
#with open("parsed_html.txt", "w") as output_file:
#   output_file.write(parsed_html_string)



#print(soup.get_text())







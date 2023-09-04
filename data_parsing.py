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
    app_description = right_side_str[0].text
    
    return {
        'category': category,
        'ranking': ranking,
        'app_name': app_name,
        'supported_languages': supported_languages,
        'pricing': pricing,
        'app_description': app_description    
    }












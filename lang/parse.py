import requests
import re
import json

r = requests.get('https://www.peppercarrot.com/en/static6/sources&page=translation')
html = r.text
langs = {}
re_lang_code_name = re.compile(r'<td>([a-z]{2}) <br/><strong>(.+?)</strong></td>')
for match in re_lang_code_name.finditer(html):
    lang_code=match.group(1)
    lang_name=match.group(2).strip()
    lang_translators = ''
    re_lang_translators = re.compile(r'<p>' + lang_name + ': (.+?)</p>')
    match_tr = re_lang_translators.search(html)
    if match_tr:
        lang_translators = match_tr.group(1)
    
    langs[lang_code] = {'name' : lang_name, 'iso_code' : '', 'translators': lang_translators}

with open('lang.json', 'w') as fp:
    json.dump(langs, fp, indent=2)
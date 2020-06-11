#!/usr/bin/env python
from pathlib import Path
import json

BASE_URL='https://gitlab.com/intangiblerealities/narupacloud/narupa-cloud-simulation-inputs/-/raw/json/'

here = Path('.')
all_xml = here.glob('*.xml')

manifest = []
for xml in all_xml:
    name = xml.stem
    content = {
        'description': 'Lorem ipsum dolor sit amet.',
        'simulation': BASE_URL + str(xml),
    }
    for runner in ('ase', 'omm'):
        json_path = xml.with_suffix(f'.{runner}.json')
        content['runner'] = runner
        content['name'] = f'{name}-{runner}'
        manifest.append(json_path)
        with open(json_path, 'w') as outfile:
            json.dump(content, outfile)

with open('manifest.txt', 'w') as outfile:
    for path in manifest:
        print(path, file=outfile)


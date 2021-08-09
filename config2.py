"""Config info."""

from collections import namedtuple

Device = namedtuple('Device', ['key', 'colour'])

# Fetch credentials and device info from environment.
AUTH_CREDS = {
    'key_id': 'c3najkv6lft00083mnn0',
    'secret': '6d21167ebfcb49ae904a016674f31613',
    'email': 'c3na40t49vq000bpt3a0@bpj7h50g7oei85t259u0.serviceaccount.d21s.com',
}

PROJECT_ID = 'bpj7h50g7oei85t259u0'

DEVICES = {
    'Thermostat': Device('bjr4af67gpvg00ck0av0', 'black'),
    'Vent': Device('bjr2615ntbig00f93asg', 'red'),
    'Piano': Device('bjr4d45ntbig00f93vh0', 'orange'),
    'Kitchen': Device('bjr445tntbig00f93t30', 'orange'),
    'Hallway': Device('bjr23oe7gpvg00cjvm60', 'green'),
    'TV room': Device('bjr4arlntbig00f93v1g', 'green'),
    'Office': Device('bjr4548pismg008i2ie0', 'green'),
    'Outside(N)': Device('bjr49pdp0jt000a5hmb0', 'blue'),
    'Outside (S)': Device('bjr449dp0jt000a5hkkg', 'blue')
}
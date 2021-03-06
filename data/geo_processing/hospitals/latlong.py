import json

latlong_dict = {'Morriston Hospital - Major': (51.684662, -3.935273), 
	'Princess Of Wales Hospital - Major': (51.517463, -3.571647),
	'Neath Port Talbot Hospital - Minor': (51.599336, -3.800879),
	'Singleton Hospital - Minor': (51.609647, -3.985408),
	'Nevill Hall Hospital - Major': (51.825082, -3.034565),
	'Royal Gwent Hospital - Major': (51.579779, -2.994478),
	'Aneurin Bevan LHB MIUs - Minor': (55.865604, -3.998619),
	'Ysbyty Ystrad Fawr - Minor': (51.633630, -3.235645),
	'Wrexham Maelor Hospital - Major': (53.046918, -3.008389),
	'Ysbyty Glan Clwyd - Major': (53.272107, -3.495894),
	'Ysbyty Gwynedd - Major': (53.209007, -4.159820),
	'Llandudno General Hospital - Minor': (53.311447, -3.827714),
	'Betsi Cadwaladr University LHB MIUs - Minor': (53.209002, -4.159590),
	'University Hospital Of Wales - Major': (51.507018, -3.190343),
	'Cardiff and Vale University LHB MIUs - Minor': (51.449635, -3.203941),
	'Prince Charles Hospital - Major': (51.763922, -3.385956),
	'The Royal Glamorgan Hospital - Major': (51.546934, -3.391817),
	'Cwm Taf LHB MIUs - Minor': (51.636495, -3.450172),
	'Bronglais General Hospital - Major': (52.416036, -4.071668),
	'Glangwili General Hospital - Major': (51.868218, -4.283960),
	'Withybush General Hospital - Major': (51.812668, -4.965219),
	'Hywel Dda LHB MIUs - Minor': (51.877202, -4.582024),
	'Prince Philip Hospital - Minor': (51.691615, -4.135931),
	'Powys Teaching LHB MIUs - Minor': (52.008661, -3.259053),
	'Morriston Hospital': (51.684662, -3.935273), 
	'Princess Of Wales Hospital': (51.517463, -3.571647),
	'Neath Port Talbot Hospital': (51.599336, -3.800879),
	'Singleton Hospital': (51.609647, -3.985408),
	'Nevill Hall Hospital': (51.825082, -3.034565),
	'Royal Gwent Hospital': (51.579779, -2.994478),
	'Aneurin Bevan LHB MIUs': (55.865604, -3.998619),
	'Ysbyty Ystrad Fawr': (51.633630, -3.235645),
	'Wrexham Maelor Hospital': (53.046918, -3.008389),
	'Ysbyty Glan Clwyd': (53.272107, -3.495894),
	'Ysbyty Gwynedd': (53.209007, -4.159820),
	'Llandudno General Hospital': (53.311447, -3.827714),
	'Betsi Cadwaladr University LHB MIUs': (53.209002, -4.159590),
	'University Hospital Of Wales': (51.507018, -3.190343),
	'Cardiff and Vale University LHB MIUs': (51.449635, -3.203941),
	'Prince Charles Hospital': (51.763922, -3.385956),
	'The Royal Glamorgan Hospital': (51.546934, -3.391817),
	'Cwm Taf LHB MIUs': (51.636495, -3.450172),
	'Bronglais General Hospital': (52.416036, -4.071668),
	'Glangwili General Hospital': (51.868218, -4.283960),
	'Withybush General Hospital': (51.812668, -4.965219),
	'Hywel Dda LHB MIUs': (51.877202, -4.582024),
	'Prince Philip Hospital': (51.691615, -4.135931),
	'Powys Teaching LHB MIUs': (52.008661, -3.259053)
}

with open('latlong_dict.json', 'w') as outfile:
	json.dump(latlong_dict, outfile)
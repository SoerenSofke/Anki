import genanki
import glob
from pathlib import Path
import random


title = 'Deutschlands Bundesländer'

aDeck = genanki.Deck(
    2059400110,
    title)

# location to name
aModel = genanki.Model(
    1607392319,
    title,
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card Number',
            'qfmt': '{{Question}}',
            'afmt': '{{Answer}}',
        },
    ],
    css='.card {font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white; }'
)

filenames = glob.glob('./federalStates/*.svg')
shuffledFilesnames = random.sample(filenames, len(filenames))

# location to name
for filename in shuffledFilesnames:
    federalState = Path(filename).stem
    aDeck.add_note(
        genanki.Note(
            model=aModel,
            fields=[
                'Wie heißt das rot markierte Bundesland?<br><br><img src="' + federalState + '.svg">',
                'Wie heißt das rot markierte Bundesland?<br><br><img src="' + federalState + '.svg"><br><br><U>' + federalState + '</U>']
        ))

# name to location
for filename in shuffledFilesnames:
    federalState = Path(filename).stem
    aDeck.add_note(
        genanki.Note(
            model=aModel,
            fields=[
                'Wo liegt das Bundesland <U>' + federalState + '</U>?<br><br><img src="Deutschland.svg">',
                'Wo liegt das Bundesland <U>' + federalState + '</U>?<br><br><img src="' + federalState + '.svg">']
        ))


filenames.append('./germanyEmpty/Deutschland.svg')

aPackage = genanki.Package(aDeck)
aPackage.media_files = filenames
aPackage.write_to_file(title + '.apkg')

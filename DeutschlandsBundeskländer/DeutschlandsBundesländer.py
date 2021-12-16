import genanki
import glob
from pathlib import Path
import random

def readSvg():
    return Path('./germanyEmpty/Deutschland.svg').read_text()

def highlight(name):
    return """
    <script type="text/javascript">
        document.getElementById("DUMMY").setAttributeNS(null, "fill", "#f00")
    </script>    
        """.replace('DUMMY', name)

def hightlightOnMap(name):
    return readSvg() + highlight(name)


def generateAnki():
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

    aDeck.add_note(
        genanki.Note(
            model=aModel,
            fields=[
                'Wie heisst das rot markierte Bundesland?<br><br>' + hightlightOnMap('MECKLENBURGVORPOMMERN'),
                'Wie heisst das rot markierte Bundesland?<br><br>' + hightlightOnMap('MECKLENBURGVORPOMMERN') + '<hr id=answer>MECKLENBURGVORPOMMERN']
        ))

    aPackage = genanki.Package(aDeck)
    aPackage.write_to_file(title + '.apkg')


def main():
    generateAnki()


if __name__ == "__main__":
    main()

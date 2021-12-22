import genanki
import glob
from pathlib import Path
import random

def generateAnki():
    random.seed(42)

    title = 'Deutschland - Stadt, Land, Fluss'

    aDeck = genanki.Deck(
        2059400110,
        title)

    # location to name
    aModel = genanki.Model(
        1607392319,
        title,
        fields=[
            {'name': 'Question'},
            {'name': 'MapStyle'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card Number',
                'qfmt': '{{Question}}<br><br>{{MapStyle}}<div id="inline-svg"></div><script src="https://raw.githack.com/SoerenSofke/Anki/feature/setSvgAttribute/DeutschlandsBundeskl%C3%A4nder/inline-svg.js"></script>',
                'afmt': '{{Question}}<br><br>{{MapStyle}}<div id="inline-svg"></div><script src="https://raw.githack.com/SoerenSofke/Anki/feature/setSvgAttribute/DeutschlandsBundeskl%C3%A4nder/inline-svg.js"></script><hr id=answer><u>{{Answer}}</u>',
            },
        ],
        css='''
        .card {
            font-family: arial; 
            font-size: 20px; 
            text-align: center; 
            color: black; 
            background-color: white; 
        }

        hr#answer {
            visibility: hidden;
        }            
        '''
    )

    states = [  
        "Niedersachsen", 
        "Hamburg", 
        "Brandenburg", 
        "Berlin", 
        "Saarland", 
        "Hessen", 
        "Bremen", 
        "Nordrhein-Westfalen", 
        "Rheinland-Pfalz", 
        "Sachsen", 
        "Schleswig-Holstein", 
        "Thüringen", 
        "Mecklenburg-Vorpommern", 
        "Bayern", 
        "Baden-Wuerttemberg", 
        "Sachsen-Anhalt", 
    ]
    random.shuffle(states)

    for state in states:
        question = 'Wie heißt das rot markierte <u>Bundesland</u>?'
        mapStyle = '<style>#State_' + state + ' {fill: crimson;}</style>'
        answer = state

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyle,
                    answer,
                    ]
            ))

    cities = [
        'Bremen', 
        'Berlin', 
        'Hamburg', 
        'Dresden', 
        'Düsseldorf', 
        'Erfurt', 
        'Hannover', 
        'Kiel', 
        'Magdeburg', 
        'Mainz', 
        'München', 
        'Saarbrücken', 
        'Schwerin', 
        'Stuttgart', 
        'Wiesbaden', 
        'Potsdam', 
    ]
    random.shuffle(cities)

    for city in cities:
        question = 'Wie heißt die rot markierte <u>Landeshauptstadt</u>?'
        mapStyle = '<style>#City_' + city + ' {fill: crimson;} #Cities {visibility: visible;}</style>'
        answer = city

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyle,
                    answer,
                    ]
            ))
    
    mountains = [
        'Teutoburger_Wald', 
        'Rothaargebirge', 
        'Westerwald', 
        'Eifel', 
        'Taunus', 
        'Odenwald', 
        'Hunsrück', 
        'Vogelsberg', 
        'Rhön', 
        'Thüringer_Wald', 
        'Erzgebirge', 
        'Fichtelgebirge', 
        'Oberpfälzer_Wald', 
        'Fränkische_Alb', 
        'Bayerischer_Wald', 
        'Schwäbische_Alb', 
        'Schwarzwald', 
        'Alpenvorland', 
        'Spessart', 
        'Harz', 
    ]
    random.shuffle(mountains)

    for mountain in mountains:
        question = 'Wie heißt das rot markierte <u>Gebirge</u>?'
        mapStyle = '<style>#Mountain_' + mountain + ' {fill: crimson;} #Mountains {visibility: visible;}</style>'
        answer = mountain.replace('_', ' ')

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyle,
                    answer,
                    ]
            ))

    rivers = [
        'Donau', 
        'Lech', 
        'Isar', 
        'Inn', 
        'Rhein', 
        'Neckar', 
        'Main', 
        'Ems', 
        'Weser', 
        'Werra', 
        'Ruhr', 
        'Oder', 
        'Saale', 
        'Mosel', 
        'Spree', 
        'Neisse', 
        'Lippe', 
        'Havel', 
        'Elbe', 
        'Fulda', 
        'Aller', 
        'Mulde', 
        'Unstrut', 
        'Peene', 
        'Naab', 
        'Lahn', 
        'Leine', 
        'Regnitz', 
        'Salzach', 
    ]
    random.shuffle(rivers)

    for river in rivers:
        question = 'Wie heißt der rot markierte <u>Fluss</u>?'
        mapStyle = '<style>#River_' + river + ' {stroke: crimson; stroke-width: 5} #Rivers {visibility: visible;}</style>'
        answer = river

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyle,
                    answer,
                    ]
            ))

    nations = [
        'Tschechien', 
        'Österreich', 
        'Frankreich', 
        'Schweiz', 
        'Polen', 
        'Belgien', 
        'Luxemburg', 
        'Niederlande', 
        'Dänemark', 
    ]
    random.shuffle(nations)

    for nation in nations:
        question = 'Wie heißt das rot markierte <u>Nachbarland</u> Deutschlands?'
        mapStyle = '<style>#Nation_' + nation + ' {fill: crimson;} </style>'
        answer = nation

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyle,
                    answer,
                    ]
            ))    

    aPackage = genanki.Package(aDeck)
    aPackage.write_to_file(title + '.apkg')


def main():
    generateAnki()


if __name__ == "__main__":
    main()

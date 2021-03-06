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
            {'name': 'MapStyleQ'},            
            {'name': 'Answer'},
            {'name': 'MapStyleA'},
        ],
        templates=[
            {
                'name': 'Card Number',
                'qfmt': '{{Question}}<br><br>{{MapStyleQ}}<div id="inline-svg"></div><script src="https://rawcdn.githack.com/SoerenSofke/Anki/release/v1.0.0/DeutschlandStadtLandFluss/inline-svg.js"></script>',
                'afmt': '{{Question}}<br><br>{{MapStyleA}}<div id="inline-svg"></div><script src="https://rawcdn.githack.com/SoerenSofke/Anki/release/v1.0.0/DeutschlandStadtLandFluss/inline-svg.js"></script><hr id=answer><u>{{Answer}}</u>',
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
        "Baden-Württemberg", 
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
                    mapStyle,
                    ]
            ))

    for state in states:
        question = 'Wo liegt das Bundesland <u>' + state +'</u>?'
        mapStyleQ = '<style></style>'
        answer = ''
        mapStyleA = '<style>#State_' + state + ' {fill: crimson;}</style>'

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyleQ,
                    answer,
                    mapStyleA,
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
        question = 'Wie heißt die rot markierte <u>Stadt</u>?'
        mapStyle = '<style>#City_' + city + ' {fill: crimson;} #Cities {visibility: visible;}</style>'
        answer = city

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyle,
                    answer,
                    mapStyle
                    ]
            ))

    for city in cities:
        question = 'Wo liegt die Stadt <u>' + city +'</u>?'
        mapStyleQ = '<style>#Cities {visibility: visible;}</style>'
        answer = ''
        mapStyleA = '<style>#City_' + city + ' {fill: crimson;} #Cities {visibility: visible;}</style>'

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyleQ,
                    answer,
                    mapStyleA
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
                    mapStyle
                    ]
            ))
    
    for mountain in mountains:
        question = 'Wo liegt das Gebirge <u>' + mountain.replace('_', ' ') +'</u>?'
        mapStyleQ = '<style>#Mountains {visibility: visible;}</style>'
        answer = ''
        mapStyleA = '<style>#Mountain_' + mountain + ' {fill: crimson;} #Mountains {visibility: visible;}</style>'

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyleQ,
                    answer,
                    mapStyleA
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
                    mapStyle
                    ]
            ))

    for river in rivers:
        question = 'Wo liegt der Fluss <u>' + river +'</u>?'
        mapStyleQ = '<style>#Rivers {visibility: visible;}</style>'
        answer = ''
        mapStyleA = '<style>#River_' + river + ' {stroke: crimson; stroke-width: 5} #Rivers {visibility: visible;}</style>'

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyleQ,
                    answer,
                    mapStyleA
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
        question = 'Wie heißt das rot markierte <u>Land</u>?'
        mapStyle = '<style>#Nation_' + nation + ' {fill: crimson;} </style>'
        answer = nation

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyle,
                    answer,
                    mapStyle
                    ]
            ))

    for nation in nations:
        question = 'Wo liegt der Land <u>' + nation +'</u>?'
        mapStyleQ = '<style></style>'
        answer = ''
        mapStyleA = '<style>#Nation_' + nation + ' {fill: crimson;} </style>'

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    mapStyleQ,
                    answer,
                    mapStyleA
                    ]
            ))            

    aPackage = genanki.Package(aDeck)
    aPackage.write_to_file(title + '.apkg')


def main():
    generateAnki()


if __name__ == "__main__":
    main()

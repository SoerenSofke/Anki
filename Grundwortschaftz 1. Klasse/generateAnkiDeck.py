import genanki
import random
import glob
import os

def generateAnki():    
    title = 'Grundwortschaftz 1. Klasse'
    random.seed(title)  

    aDeck = genanki.Deck(
        random.randrange(2**32),
        title)

    # location to name
    aModel = genanki.Model(
        random.randrange(2**32),
        title,
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card Number',
                'qfmt': '<br><br><br>{{Question}}',
                'afmt': '<br><br><br>{{Question}}<br>{{Answer}}',
            },
        ],
        css='''
        .card {
            font-family: arial; 
            font-size: 8vw; 
            font-weight: bold;
            text-align: center; 
            color: black; 
            background-color: white; 
        }

        hr#answer {
            visibility: hidden;
        }            
        '''
    )

    filenames = glob.glob('audio/*.ogg')    
    basenames = []

    random.shuffle(filenames)
    for filename in filenames:

        filename = os.path.basename(filename)
        basenames.append(filename)

        question = filename.replace('.ogg', '')
        question = question.replace(' (', '<br>(')
        answer = '[sound:' + filename + ']'

        aDeck.add_note(
            genanki.Note(
                model=aModel,
                fields=[                
                    question,
                    answer,
                    ]
            ))  

    aPackage = genanki.Package(aDeck)
    aPackage.media_files = filenames
    aPackage.write_to_file(title + '.apkg')


def main():
    generateAnki()


if __name__ == "__main__":
    main()

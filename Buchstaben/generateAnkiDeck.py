import genanki
import random
import glob

def generateAnki():
    random.seed(42)

    title = 'Alphabet'

    aDeck = genanki.Deck(
        2059400111,
        title)

    # location to name
    aModel = genanki.Model(
        1607392320,
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
        css='''
        .card {
            font-family: arial; 
            font-size: 70vh; 
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

    filenames = glob.glob('*.svg')
    print(filenames)

    for filename in filenames:        
        question = filename[0]
        answer = '<img src="' + filename + '">'

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

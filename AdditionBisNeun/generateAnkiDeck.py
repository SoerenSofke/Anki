import genanki
import random
import glob


def generateAnki():
    random.seed(42)

    title = 'Addition bis 9'

    aDeck = genanki.Deck(
        2059400112,
        title)

    # location to name
    aModel = genanki.Model(
        1607392321,
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
            font-size: 10vh; 
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

    for x in range(0, 9):
        for y in range(0, 9):
            equation = '{{c3:: ' + str(x) + '}} + {{c2::' + str(y) + '}} = {{c1::' + str(x+y) + '}}'     

            aDeck.add_note(
                genanki.Note(
                    model=genanki.CLOZE_MODEL,
                    fields=[equation]
                ))

    aPackage = genanki.Package(aDeck)
    aPackage.write_to_file(title + '.apkg')


def main():
    generateAnki()


if __name__ == "__main__":
    main()

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
            {'name': 'Text'},
        ],
        templates=[
            {
                'name': 'Card Number',
                'qfmt': '<br><br><br>{{cloze:Text}}',
                'afmt': '<br><br><br>{{cloze:Text}}',
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

        .cloze {
            font-weight: bold;
            color: blue;
        }           
        '''
    )

    for x in range(0, 9):
        for y in range(0, 9):
            equation = '{{c3:: ' + str(x) + '}} + {{c2::' + str(y) + '}} = {{c1::' + str(x+y) + '}}'     

            aDeck.add_note(
                genanki.Note(
                    model=aModel,
                    fields=[equation]
                ))

    aPackage = genanki.Package(aDeck)
    aPackage.write_to_file(title + '.apkg')


def main():
    generateAnki()


if __name__ == "__main__":
    main()

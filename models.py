import genanki

my_model = genanki.Model(
    1979232991,
    'Simple Model',
    fields = [
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        }
    ],
)
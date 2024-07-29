import genanki
from axioms_deck import axioms_deck

genanki.Package(axioms_deck).write_to_file('output.apkg')
import genanki
from models import my_model

metagraph = genanki.Note(
    model = my_model,
    fields = ['metagraph', r'\begin{tikzcd} a \arrow[r, "f"] & b \end{tikzcd}']
)

from flask import Blueprint, render_template, request

from app.dex.forms import PokedexEntry

dex = Blueprint('dex', __name__, template_folder='dex_templates')

@dex.route('/pokedex')
def pokedex():
    form = PokedexEntry()
    if request.method == 'POST':
        if form.validate():
            entry = form.entry.data
    return render_template('pokedex.html', form=form)
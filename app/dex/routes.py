from urllib import response, request
from flask import Blueprint, render_template, request, url_for
from flask_login import login_required

from app.dex.forms import PokedexEntry

import urllib.request, json

from app.models import Pokedex

dex = Blueprint('dex', __name__, template_folder='dex_templates')

@dex.route('/pokedex', methods=['GET', 'POST'])
@login_required
def pokedex():
    form = PokedexEntry()
    if request.method == 'POST':
        if form.validate():
            entry = form.entry.data

            url = f'https://pokeapi.co/api/v2/pokemon/{entry}'
            response = requests.get(url)
            if response.ok == True:

                type = response.json()['types']['type']['name']
                print(type)
                ability = response.json()['abilities'][0]['ability']['name']
                print(ability)
                img_url = response.json()['sprites']['front_default']
                hp = response.json()['stats'][0]['base_stat']
                attack = response.json()['stats'][1]['base_stat']
                defense = response.json()['stats'][2]['base_stat']
                special_attack = response.json()['stats'][3]['base_stat']
                special_defense = response.json()['stats'][4]['base_stat']
                speed = response.json()['stats'][5]['base_stat']

            pokedex = Pokedex(entry, img_url, type, ability, hp, attack, defense, special_attack, special_defense, speed)

            pokedex.save_to_db()

            


    return render_template('pokedex.html', form=form)


@dex.pokeview('/Pokebox')
def pokeview():
    boxs = Pokedex.query.all()
    print(boxs)
    return render_template('pokeview.html', boxs=boxs)


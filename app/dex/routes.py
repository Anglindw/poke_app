
from flask import Blueprint, Request, render_template, request, url_for, request_started, request_finished, redirect
from flask_login import current_user, login_required
from app.dex.forms import PokedexEntry
from app.models import Pokedex
import requests

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
                img_url = response.json()['sprites']['front_default']
                print(type)
                ability = response.json()['abilities'][0]['ability']['name']
                print(ability)
                hp = response.json()['stats'][0]['base_stat']
                attack = response.json()['stats'][1]['base_stat']
                defense = response.json()['stats'][2]['base_stat']
                special_attack = response.json()['stats'][3]['base_stat']
                special_defense = response.json()['stats'][4]['base_stat']
                speed = response.json()['stats'][5]['base_stat']

                pokedex = Pokedex(entry, img_url, ability, hp, attack, defense, special_attack, special_defense, speed, current_user.id)

                pokedex.save_to_db()

                return redirect(url_for('dex.pokeview'))

            


    return render_template('pokedex.html', form=form)


@dex.route('/pokedex/view')
def pokeview():
    boxs = Pokedex.query.all()
    print(boxs)
    return render_template('pokeview.html', boxs=boxs[::-1])

@dex.route('/pokedex/<int:pokedex_id>')
def view_entry(pokedex_id):
    post = Pokedex.query.get(pokedex_id)
    if post:
        return render_template('pokemon_summary.html', post=post)
    else:
        return redirect(url_for('dex.pokeview'))

@dex.route('/pokedex/delete/<int:pokedex_id>')
def delete_poke(pokedex_id):
    post = Pokedex.query.get( pokedex_id )
    if current_user.id == post.user_id:
        post.delete_from_db()
    else:
        return redirect(url_for('dex.pokeview'))


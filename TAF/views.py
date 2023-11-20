from django.shortcuts import render
import requests
from items.models import cuisines, dishes

api_key = '6ed583ee713f4addb3483d438948fe1d'


search_url = 'https://api.spoonacular.com/recipes/search'


def home(request):
    return render(request, 'index.html')


def auth(request):
    return render(request, 'TAFlog.html')


def cuisine(request, val):
    cuisses = cuisines.objects.all()
    con = {'val': val, 'cuisses': cuisses}
    return render(request, 'cuis.html', con)


def item(request, val):
    dishe = dishes.objects.filter(category=val).all()
    con = {'cuis': val, 'dishe': dishe}
    return render(request, 'dishes.html', con)


def recipe(request, val1, val2):
    dish_name = val2
    search_params = {
        'apiKey': api_key,
        'query': dish_name,
        'number': 1,
    }
    search_response = requests.get(search_url, params=search_params)

    if search_response.status_code == 200:

        search_data = search_response.json()

        if 'results' in search_data and search_data['results']:
            dish_id = search_data['results'][0]['id']
            url1 = f'https://api.spoonacular.com/recipes/{dish_id}/information'

            params = {
                'apiKey': api_key,
                'includeNutrition': False,
            }

            response = requests.get(url1, params=params)
            if response.status_code == 200:

                recipe_info = response.json()
                if 'extendedIngredients' in recipe_info:
                    # dish_id = recipe_info['results'][0]['dish_id']
                    nam = dish_name
                    cuis = val1
                    im = recipe_info['image']
                    newe = dishes(category=cuis, Name=nam, bg=im)
                    existing_dish = dishes.objects.filter(
                        Name=nam, category=cuis).first()

                    if existing_dish is None:
                        # Dish doesn't exist, create a new entry

                        newe.save()
                    ingredients = recipe_info['extendedIngredients']
                    con = {'cuis': cuis, 'name': nam,
                           'time': recipe_info['readyInMinutes'], 'ingr': ingredients, 'bg': im}
                    return render(request, 'desc.html', con)
                else:
                    return render(request, 'nofood1.html')
            else:
                return render(request, 'nofood1.html')
        else:
            print(f"No results found for '{dish_name}'.")
    else:

        return render(request, 'nof2.html')

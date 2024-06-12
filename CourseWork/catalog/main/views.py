from django.shortcuts import render


def show_main(request):
    data = {
        'products': [
            {
                'name': 'Линолеум бытовой Tarkett Stimul Pegas 1 (3м)',
                'price': 1389,
                'width': 300,
                'thickness': 2.0,
                'safe_layer': 0.15,
                'fire_safety': 'КМ5',
                'brand': 'Tarkett',
                'link': 'https://vladivostok.pol-doma.com/catalog/napolnye_pokrytiya/linoleum/bytovoy_linoleum/45686/',
                'photo': 'https://vladivostok.pol-doma.com/upload/iblock/75f/Tarkett-Stimul-Pegas1.jpg'
            },
            {
                'name': 'Линолеум бытовой Tarkett Evolution Raymond 4 (3,5м)',
                'price': 1771,
                'width': 350,
                'thickness': 2.7,
                'safe_layer': 0.2,
                'fire_safety': 'КМ5',
                'brand': 'Tarkett',
                'link': 'https://vladivostok.pol-doma.com/catalog/napolnye_pokrytiya/linoleum/bytovoy_linoleum/45416/',
                'photo': 'https://vladivostok.pol-doma.com/upload/iblock/482/Tarkett-Evolution-Raymond4.jpg'
            },
            {
                'name': 'Линолеум бытовой Tarkett Evolution Palladio 20 (3,5м)',
                'price': 1771,
                'width': 350,
                'thickness': 2.7,
                'safe_layer': 0.2,
                'fire_safety': 'КМ5',
                'brand': 'Tarkett',
                'link': 'https://vladivostok.pol-doma.com/catalog/napolnye_pokrytiya/linoleum/bytovoy_linoleum/45408/',
                'photo': 'https://vladivostok.pol-doma.com/upload/iblock/7ae/Tarkett-Evolution-Palladio20.jpg'
            },
            {
                'name': 'Линолеум бытовой Tarkett Evolution Chevron 6 (3,5м)',
                'price': 1771,
                'width': 350,
                'thickness': 2.7,
                'safe_layer': 0.2,
                'fire_safety': 'КМ5',
                'brand': 'Tarkett',
                'link': 'https://vladivostok.pol-doma.com/catalog/napolnye_pokrytiya/linoleum/bytovoy_linoleum/45404/',
                'photo': 'https://vladivostok.pol-doma.com/upload/iblock/6fe/Tarkett-Evolution-Chevron6.jpg'
            }
        ]
    }
    return render(request, 'main/index.html', data)

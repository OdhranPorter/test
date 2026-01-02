from django.shortcuts import render
from recipes.models import Recipe,Ingredient,Tag, RecipeTag, RecipeIngredient, Review
from statistics import median

# Create your views here.
#Calculates median for the available ratings of the recipe
def median_rating (reviews_ratings):
    return median(reviews_ratings)

def recipes_list(request):
    recipes = Recipe.objects.all()
    recipe_list = list()
    for recipe in recipes:
        reviews = recipe.review_set.all()
        tags=recipe.tags.all()
        ingredients = recipe.ingredients.all()
        if reviews:
            review_ratings = list()
            for review in reviews:
                review_ratings.append(review.rating)
            recipe_rating = str(round(median_rating(review_ratings), 2))
            number_of_reviews = str(len(reviews))
        else:
            recipe_rating = None
            number_of_reviews="0"

        # if tags:
        #     tag_list = list()
        #     for company in production_companies:
        #         production_companies_list.append(company.production_company)
        #
        # if genres:
        #     genres_list = list()
        #     for genre in genres:
        #         genres_list.append(genre.genre)

        recipe_list.append({'recipe': recipe,\
                           'tags': tags, \
                           'ingredients': ingredients, \
                           'recipe_rating': recipe_rating,\
                          'number_of_reviews':number_of_reviews})

    context={
            'recipe_list': recipe_list
        }

    return render(request, 'recipes_list.html', context)

def details_reviews(request):
    recipe_id = request.GET.get("recipe_id")
    print(recipe_id)
    recipe=Recipe.objects.get(id=recipe_id)
    print(recipe.name)
    reviews = recipe.review_set.all()
    print(reviews)

    context={
        'recipe':recipe,\
        'reviews': reviews,
    }

    return render(request,'recipes_reviews.html', context)



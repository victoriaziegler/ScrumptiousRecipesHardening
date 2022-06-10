## Planning for shopping items

* [ ] Create model for ShoppingItem under recipes models.py
    - Include foreign keys for user and food item
    - make migrations!!!
* [ ] Create ShoppingList list.html
    - link to base.html
* [ ] Create Class ShoppingList view in recipe views.py tied to list.html
* [ ] Register class view in recipe's urls.py
* [ ] Make sure above works then add, commmit, push


* [ ] Create function view in recipe views.py to create a shopping item instance
    - This is a POST method based ont he submitted ingredient id in the form
* [ ] Register function view in recipes urls.py
* [ ] Create the add ingredient button
    - Add HTML form to ingredients table on detail page (points to URL of function view)
* [ ] Make sure above works then git add, commit, push


* [ ] Create function view in recipe views.py to delete all shopping items
    -Make sure this is just for the current user
* [ ] Register function view in recipes urls.py
* [ ] Add HTML form to top of list page (points to URL of list class view)
* [ ] Make sure above works the git add, commit, push


* [ ] Check there is no add buttom when food in shopping list
* [ ] Add list of food items in current user's list to the context of the recipe detail view
* [ ] Based on values in list, show add button if item not in list 
    - If value is in the list show the message in your list
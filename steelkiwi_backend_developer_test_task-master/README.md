
teelkiwi Python Test Task
Please fork this repository and resolve issues in the scope of this project. After having completed tasks you think are better to be done, please create a pull request and send a link to the HR you’ve been communicating with so far.
Feel free to do as much of the assignment as you can - it could be either the whole task or separate assignments from each one of its levels (see Basic and Advanced Requirements lists). You should note the parts that you have implemented in the repository’s TASKS.md file. Remember - it’s important that you do as much as you can, but it is just as important to fully demonstrate the way you think and complete tasks while still presenting clean and concise quality code.
Here you can find the ware-frames for the project.

Start project


git clone https://repo.url - clone repo

virtualenv venv --python=/path/to/python - configure virtual environment

pip install -r requirements.txt - install requirements

pip install -r requirements/local.txt - install requirements for tests

createdb test_products_task - create PostgreSQL database

cp env.example .env - crate you env file with settings

python manage.py migrate - migrate database

python manage.py runserver - run development server


General Requirements:

Use the latest version of Django.
Follow the rules of PEP8.
Display errors next to the form fields.
Use PostgreSQL as the database engine.
Use ‘base.html’ for all of the project’s templates.
You should update the ‘Requirements’ file whenever having added a dependency. You can also update any other version of this file if you think that the new version would be better than the used one.
Use English as the main language for all templates, string constants and comments.
When developing, try to avoid duplicating queries to the database. Make sure to optimize the code (with Django Debug Toolbar or any other tool, this choice is on you).
Use Django migrations for all changes in fields and models.
Use class-based views for all views on the website. If you think that using a function-based view in a particular case would be better, please do but add an explanation why in the comments.
Create fixtures or commands for data generation.


Basic Requirements:

Finish provided unit tests and add as many of them as you find necessary.
Update the field “slug” of the Product model so that it’s unique.
Add an image field to the Product model.
Implement a page that shows a list of all categories with a number of products in each. The title must be a link leading to the page with product and category details.
Implement a page that would show a list of all products in a given category with pagination. Display a title, a price, a small thumbnail and the number of likes for each product. Use the category slug in URL.
Implement a ‘Product Details’ page. Display each product’s title, image, price, description and other basic info.
Add the ability to like products, save either the account of the person that has liked something or their IP address (for unauthorized users). Allow only one like per user/IP. Do not keep IP for authenticated users.
Add the ability to comment products on their respective pages and display all recent comments (for the span of last 24 hours). The comment length should be limited to 500 symbols. Authorization should not be required, comments must be flat - ,no replies needed.
Add all models to the admin interface and make sure that the ‘view on site’ button works properly.


Advanced Requirements:

Add the WSYWIG editor to Product description.
On the main page, display the list of top 10 most popular products (as measured by the number of likes)
Add the ability for admins to add the products of their choice to the ‘Popular’ list.
Add a filter to the Django admin interface that would allow displaying only the users that haven’t left any comments and/or ratings.
Add product grade field to all products model with such choices as ‘base’, ‘standard’ and ‘premium’. Add data migration to set all products into the ‘standard’ class(grade).
On the ‘Main’ page, inside ‘Choice of week’ section, display the number of ‘base’ products (>10 likes), ‘standard’ products (>5 likes) and the total number of ‘premium’ products. In order to accomplish this task, please try to implement with the only one query to the database.
Implement page that will show a list of products by filter from previous point.
On the category page, add a price filter to the product list. It should take two inputs, minimum and maximum prices being set by default. It’s okay to reload the page on submit.
Add filters for the number of likes and comments (e.g. “show products with at least one like/comment”).
Add track of all page loads, need to save timestamp, page url,  user if authenticated and ip if not.
Add statistics by the number of page loads per day for the last week on the main page.
Implement a management command that generates the CSV with products. Columns should be ‘ID’, ‘Title’, ‘Number of Comments’, ‘Number of Likes’. Add parameters that would allow setting file destinations, not exporting products without likes and not exporting products without comments.
On each page, display a list of products in the sidebar - one from each category. New arrivals on frames.. It is better to make only one request from django for this.
Include the ability to add products to the shopping cart.
Add the ability to create orders and pay for the products in the cart through Stripe, you can use checkout.
Add a page with list of all orders made by the user, pagination is not needed.

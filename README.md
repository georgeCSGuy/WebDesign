READ ME

Once you have python installed, download flask, some other flask dependancy, and the sqlalchemy dependency using pip.  i dont remember the exact dependency names but they are in the tutorials i put in the groupchat a while back.

TO RUN: 
enter the command: 
	python app.py
go to your browser and to page: 
	0.0.0.0:4000

Test username: aaron
Test password: rotem

TODO
1. Add links to all the pdfs and images on all pages in /templates
	Every time there is a link to a file in the static folder do this:
	{{ url_for('static', filename='lesson2/someting.pdf') }}

2. Add login form to every page=> i dont know why you can only actually see it on the home page

3. I made the premium content script on the javalesson2.html page on the bottom.  need to integrate to other pages and fix css

4. Fix css for login form
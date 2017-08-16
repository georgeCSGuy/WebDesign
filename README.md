READ ME

Once you have python installed, download flask, some other flask dependancy, and the sqlalchemy dependency using pip.  i dont remember the exact dependency names but they are in the tutorials i put in the groupchat a while back.

TO RUN: 
enter the command: 
	python app.py
go to your browser and to page: 
	0.0.0.0:4000

Test username: aaron
Test password: rotem

File Structure Needed for Flask: 
/webDesign
	/dbSetupFiles 	//not necessary for the app but examples of how to use the db if we need to write more querys
	/static			//all static files go here because of flask
		/AdPlaceholders
		/images
		/lessons 	
			/Lesson1 and etc...
		/styles
	/templates		//all the html pages you see(even one line of python makes it not static)
		FrontPage.html
		JavaLesson1.html and etc...
		login.html
	app.py 			//the 'main' script file.  runs the server and etc
	tutorial.db 	//the DB file, the DB is called tutorial becasue i did it in a tutorial
	tabledef.pyc 	//required for the db to work, im not sure why

TODO
1. Add links to all the pdfs and images on all pages in /templates
	Every time there is a link to a file in the static folder do this:
	{{ url_for('static', filename='lesson2/someting.pdf') }}

2. [CSS]Add login form to every page=> i dont know why you can only actually see it on the home page

3. [PY]Instead of having different routes for each page, what about one route method with a parameter, should help with the login script too

4. [CSS]Fix css for login form

5. [CSS]Find packages/framework for the css

7.  [PY]for login route--add parameter to return back to that page

8. [CSS]Fix the css for front page
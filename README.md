csc309-a2
=========

The Tumblr Trackr: A CSC309 Web Programming Assignment

GROUP:
Francisco Canas (g1canasf)
Zizhou Wang (g2zizhou)
Zhanara Orazbayeva (g2zhan)

HOW TO RUN SERVER:
Go to the trackr root folder, and use this command:
python manage.py runserver

FILE TREE:
 trackr/ -- Project root folder.
	manage.py -- Utility used to make project setting changes.
	tempdb -- A file containing a temporary DB for testing.
	trackr/ -- Folder containing project source files.
		__init__.py -- Empty file. Informs python this folder is a package.
		settings.py -- Configuration file for project.
		urls.py -- Contains the URL service request router code!
		wsgi.py -- For WSGI projects. Don't need it for Trackr.
		handlers.py -- Code for our request handlers lives here.
		tracker.py -- Code for our blog tracking lives here.
		models.py -- Classes defined for the database to be created on syncdb



	

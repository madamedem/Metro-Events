# Metro-Events

# CLONE THIS PROJECT
1. Fork this project first:
	- Please see this [Image](https://imgur.com/Fd2omst "Image").
2.  Open Github Desktop and Clone the Repository that you **cloned**:
	> File -> Clone Repository -> URL


# Project Setup
1. Create a new database in **phpMyAdmin**
	- **Database Name:** *metro_events (or kung unsa inyo ganahan)*

2. Open the project in VS Code(**metroevents1**)
   - Right Click **metroevents1** and click **Open with Code**
   - After opening in VS Code, your file tree will look like this:
```
|-- metroevents1
  |-- metroevents1
  |-- static
  |-- user
  |-- db.sqlite3
  |-- manage.py
  |-- README.md
```

3. Open VS Code Terminal
	> Ctrl + `

	#### Enter the commands below:
`pip install django`

`pip install mysqlclient`

`python manage.py migrate`

4. Create SuperUser(using the **terminal**):
`python manage.py createsuperuser`

	#### Enter the details below:
>username: admin
>password: adminMetroEvents

# Run Project
1. Open **XAMPP Control Panel**
	>Apache -> Start
	>MySQl -> Start

1. Run the project in the **VS Code** terminal:
	 ` python manage.py runserver`

2. Open the project in your web browser:
	>127.0.0.1:8000/user/login
	
	>127.0.0.1:8000/user/register
	
	>127.0.0.1:8000/admin

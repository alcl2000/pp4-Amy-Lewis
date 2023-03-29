

- [Site Development](#site-development)
- [Design](#design-choices)
- [Testing Document](/testing.md)
- [Features](#features)
- [Technology Used](#technology-used)
- [Development](#development)
    - [Cloning](#cloning)
- [Deployment](#deployment)
- [Bug Testing](#bug-testing)
- [Credits](#credits)

## Site Development

This site was developed using the Django framework, to help wih development, I created a sitemap so that I could decide which features to implement on which page. This was important for developing templates, so I knew which pages to implement when
![A site map showing various site pages and their actions](readme/sitemap.jpg)

To better understand the mechanics of the database, I built a database schema to show the relations of the various tables and fields.
![A database schema showing my tables and their relations](readme/database-schema.jpg)

## Design Choices

The website was designed to be a bridge between retro true crime and conspiracy forums and modern micro forums like reddit. The conspiracy forums of the early internet were a gathering place for people with fringe ideas. They were often developed by people in their spare time and didn’t necessarily have dedicated development UX/UI staff. The websites were hard to navigate but were a clear passion project for those involved. More modern sites like Reddit have sprung up as a response to web 2.0 and have been developed with users in mind. They provide a more user friendly and aesthetically appealing website, at the cost of the authenticity that the underground, less polished sites provided. 

![](readme/conspiracy-forum-1.jpg)
![](readme/conspiracy-forum-2.jpg)
![](readme/conspiracy-forum-3.jpg)
![](readme/conspiracy-forum-4.jpg)

As this project is intended as an in-universe tie-in to the show yellowjackets, fonts and colours were picked from the show, to keep with the show. The show uses a dark colour palette to represent both the cult and conspiracy storylines within the show, and these were used across the site to help it feel more underground like the earlier sites. 
![The four main adult yellowjackets in front of a shadowy figure](readme/yellowjackets-1.jpg)
![Adult Shauna and Adult Misty in front of a teal background](readme/yellowjackets-2.jpg)
![Three of the teen yellowjackets on the plane before its impending crash](readme/yellowjackets-3.jpg)

Fonts were chosen mainly because of their spacing and simplicity to help with accessibility. Fira Sans Condensed is a sans-serif font which is well spaced and modern, but still looks similar to the typewriter fonts, which again speaks to the conspiracy at the heart of the show.
![The Fira Sans Condensed font from Carrois Apostrophe via Google Fonts](readme/fira-sans-condensed.jpg)

While the font 'Lobster Two' was chosen to add a design flair to the site and to match the promotional material of the show. 
![The Lobster Two font from Impallari Type via Google Fonts](readme/Lobster-two.jpg)

## Features

## Technology Used

* Django - The main framework used to create responsive web pages
* Jinja 2 - The scripting language used to combine the HTML and Django elements
* Python - Used to develop the backend of django and communicate with the database
* ElephantSQL - Used to host the main database of the site
* JavaScript - Used to add reactive elements to the front-end of the website, mainly using the Jquery framework
* Bootstrap - A CSS/HTML framework used to help with shorthand styling on across the site
* HTML - Used to create the basic skeletons of the site
* CSS - Used for styling across the site
* Cloudinary - Hosting Static files

## Bug Testing

## Development

### Creating a repository
- Either create an account or log into GitHub.com
- From your profile click the 'Repositories' section and then click the 'New' button
- Then, give your repository a unique name and open in your IDE of choice

### Forking
- From the repository page, click 'fork' at the top
- The repository will then be in your listed repositories on your profile

### Cloning
- From the top of the repository page, select the drop-down 'Code' and then pick the 'GitHub CLI' section
- Copy the command presented, and run it in the command line of your chosen IDE

## Credits

- [Auto Slug Field](https://django-autoslug.readthedocs.io/en/latest/ ) used to create auto slugs on the site
- []()

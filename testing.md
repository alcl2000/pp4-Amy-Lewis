# Testing document

-[Validators](#validators)
- [User story Testing](#user-stories-testing)
-[Manual Testing](#manual-testing)

## Validators

 -  All custom HTML pages on my site pass HTML validation from W3C 
 ![A screenshot showing the HTML validation from the W3C validator](/readme/html-validation-big.jpg)
 - My one page of CSS Passes validation from WC3 as well 
 ![A screenshot showing the CSS passing validation through the W3C validator](readme/css-validation.jpg)
 - The Jquery file has passed validation through JShint
 ![A screenshot showing the JS file passing validtion from the JShint Jquery validator](readme/jshint-validation.jpg)

 ### Python Validation
- All custom python files in the citizen_detective app pass python validation through CI's own pep8 validator
![The validation pass for admin.py](readme/admin.py-validation.jpg)
![The validation pass for forms.py](readme/forms.py-validation.jpg)
![The validation pass for models.py](readme/models.py-validation.jpg)
![The validation pass for urls.py](readme/urls.py-validation-cd.jpg)
- All the custom python files in the forum app pass python validation through CI's own pep8 validator
![The validation pass for urls.py](readme/urls.py-validation-forum.jpg)
![The validation pass for views.py](readme/views.py-testing.jpg)

## User Story Testing

- As a site user I want to be able to view all the categories on the site
  - I created the category list view to allow users to see all the categories on the site in a list, so they can pick which posts they would like to see 
- As a user I would like to be able to make a new Category for a new post type
  - I added Category CRUD functions to allow users to create different categories to sort posts by, the post model also links to the category model
- As a User I want to be able to sort posts by category so I can see the most relevant posts for my interests
  - The Category detail view was created to allow users to see the posts which are most relevant to their interests
- As a user, I want to read posts in an order that make sense
  - Users see posts on the index page and the category specific views in chronological order
- As a user I want to be able to CRUD my own posts, when logged in, without having to log into an admin panel
  - A post making form was added to the index page to allow users to create their own posts; they can edit or delete the posts when logged in through a toggle to the side of the post
- As a User I want to be able to leave comments on other people's posts 
  - A comment form was added to the post-detail view, allowing users to leave comments on every single post on the site
- As a User I want to be able to like and rate posts
  - Users, when logged in, can add likes to posts to show their appreciation 
- As a User I want to recieve meaningful feeback when I interact with posts on the site, or run into issues so I understand what's happening during certain processes
  - Users are given feedback whenever they enter information, both through Jquery and Django's messages framework
  - This ensures that they understand which actions are being taken and feel as though they are properly interacting with the site
- 


## Manual Testing

### Nav Bar 


<table>
  <tr>
   <td>Feature 
   </td>
   <td>Indented action
   </td>
   <td>Actual Action
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Site logo
   </td>
   <td>When the site logo is clicked, it returns the user to the index page
   </td>
   <td>When clicked, the user is redirected to the index page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Account Button
   </td>
   <td>When the link is clicked, the user is taken to the sign up page
   </td>
   <td>When the button is clicked, the sign up page is returned
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Login button - user logged out
   </td>
   <td>If a user is logged out the final link on the nav bar directs them to log in 
   </td>
   <td>When a user is not logged in the final link on the nav bar reads ‘log in’ and directs them to the log in page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Logout button - user logged in
   </td>
   <td>If a user is logged in, the final navbar link directs them to log out 
   </td>
   <td>When a user is not logged in, the final link on the nav bar reads ‘log out’ and directs them to the log out page 
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Index


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Action
   </td>
   <td>Actual Action 
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Post link in title
   </td>
   <td>When the link in the title is clicked it takes you to the post detail view using the post’s slug to view the post detail
   </td>
   <td>Clicking the link takes you to the post detail view 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post ‘like button’
   </td>
   <td>If a user is logged in, the form posts and the user’s like is added to the post like count
   </td>
   <td>The like is added when a logged in user clicks the button
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post ‘like button’
   </td>
   <td>If a user is not logged in, the form does not post and instead a dropdown appears telling them to log in
   </td>
   <td>When a user is not logged in, they are asked to log in before liking a post
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post ‘comment’ button
   </td>
   <td>If a user clicks the comment button from the index page it takes them to the post detail page and directs them to the comment form
   </td>
   <td>When the comment button is clicked they are redirected to the post’s comment section
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Make Post From
   </td>
   <td>If a user is logged in they can make a post 
   </td>
   <td>When logged in a user can make a post
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Make Post Form
   </td>
   <td>If a user is not logged in they cannot make a post 
   </td>
   <td>When logged out, users cannot make posts
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>-
   </td>
   <td>Input validation - Title
   </td>
   <td>A title must be entered to post the form
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>-
   </td>
   <td>Input validation - Category
   </td>
   <td>A category must be selected to make the post 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>-
   </td>
   <td>Input validation - Tag
   </td>
   <td>A tag must be selected to make the post
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>-
   </td>
   <td>Input Validation - Post
   </td>
   <td>A post must be written for the post to be made
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Category List Link
   </td>
   <td>When a user clicks the link they are able to view the category list view 
   </td>
   <td>When the link is clicked, the user is redirected
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Category Link
   </td>
   <td>If the link is clicked, it should use that categories’ slug to take the user to the category detail view, which shows them the content in a specific category
   </td>
   <td>When the link is clicked, the user is redirected 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post drop down - edit function
   </td>
   <td>If a user is a staff member, or the creator of a post, they are able to edit the post 
   </td>
   <td>When the user who created the post or a staff member is logged in, they are able to edit a post 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post drop down - delete function
   </td>
   <td>If a user is a staff member or the creator of a post, they are able to delete the post
   </td>
   <td>If a user is logged in as staff or the creator of a post, they are able to delete the post after pressing a JQuery confirmation
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Post detail


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Action
   </td>
   <td>Actual Action
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>‘Post Like’ function
   </td>
   <td>If a user is logged in they are able to interact with the post like form and add their like to a post 
   </td>
   <td>When a logged in user clicks the like button, their like is added to a post
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>‘Post Like’ function
   </td>
   <td>If a user is not logged in they cannot use the form 
   </td>
   <td>If a user is not logged in, a dropdown appears to inform them they need to log in to interact with the post 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Comment form -Logged in 
   </td>
   <td>When user is logged in, they are able to leave a comment on the post 
   </td>
   <td>When logged in, a user may leave a comment
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Comment form - Not logged in 
   </td>
   <td>When logged out, a user cannot access the comment form 
   </td>
   <td>When logged out, a user may not try to leave a comment
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Comment form - validation 
   </td>
   <td>A user cannot make an empty comment
   </td>
   <td>A user may not post a comment without any content
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Comment drop down delete
   </td>
   <td>If a user is logged in as staff or the creator of the comment, they are able to delete the comment
   </td>
   <td>If the user who create the comment or a staff member is logged in, they are able to delete a comment
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post drop down - edit function
   </td>
   <td>If a user is a staff member, or the creator of a post, they are able to edit the post
   </td>
   <td>When the user who created the post or a staff member is logged in, they are able to edit a post 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post drop down - delete function
   </td>
   <td>If a user is a staff member or the creator of a post, they are able to delete the post
   </td>
   <td>If a user is logged in as staff or the creator of a post, they are able to delete the post after pressing a JQuery confirmation
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Post edit


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Post Edit form validation - Title
   </td>
   <td>A user cannot submit the post without adding a title and the form will not post 
   </td>
   <td>The post does not submit and asks the user to add a title before posting
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post Edit form validation - Tag
   </td>
   <td>A user cannot submit the post with the tag field empty 
   </td>
   <td>The post does not submit and the user is prompted to add one before posting
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post Edit form validation - Category
   </td>
   <td>A user cannot submit the post with the category field empty 
   </td>
   <td>The post does not submit without a category and is prompted to select one before posting
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post Edit form validation - Content
   </td>
   <td>A user cannot submit the post with the content field empty
   </td>
   <td>The post does not submit with the content field empty and are prompted to add some before posting
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Redirection
   </td>
   <td>After the form is correctly entered and submitted, the user is redirected back to the post view they came from 
   </td>
   <td>When the correct form is submitted the user is redirected to the post detail view of the post they edited
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Category Detail View


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Add Tag button
   </td>
   <td>If a user clicks the add tag button they are taken to the add tag page
   </td>
   <td>When the add tag button is clicked, the user is redirected to the add tag page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Post detail link
   </td>
   <td>If a user clicks the link in the post title, they are taken to the post detail view
   </td>
   <td>When the title is clicked, the user is taken to the post detail view
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>‘Post Like’ function
   </td>
   <td>If a logged out user clicks the post like function, they are asked to log in
   </td>
   <td>When a logged out user clicks the button, they are directed to log in to ‘like’ the post
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>‘Post Like’ function
   </td>
   <td>If a user is logged in they can submit the form and either add or remove their like from the post 
   </td>
   <td>When logged in the form submits and and the user and can either add or remove their like from a post 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>‘Post Comment’ button
   </td>
   <td>When a user clicks the post comment button they are taken to the post detail view and the comment section
   </td>
   <td>On click, a user is taken to the post detail view and comment section
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Back to category page link
   </td>
   <td>When a user clicks the link it should take them to the category list page 
   </td>
   <td>When a link is clicked, the user is taken to the category list page
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Category List View


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Category detail link
   </td>
   <td>When the link in the card of each category is clicked, it takes the user to the category detail page for that category
   </td>
   <td>When the title of the category detail card clicked, the user is taken to a category detail view
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Add Category Link
   </td>
   <td>When the link is clicked, the user is redirected to the add category page
   </td>
   <td>On clicking, the user gets redirected to the add tag page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Logged in user, Category drop down 
   </td>
   <td>If a user is logged in, they are able to toggle the dropdown 
   </td>
   <td>When logged in the dropdown toggles and allows for selection from other menus
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Logged out user, category drop down
   </td>
   <td>If a user is not logged in, they are unable to activate the toggle
   </td>
   <td>Logged out users cannot use the dropdown
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Logged in User, Category Edit link
   </td>
   <td>If the user is logged in, they can use the toggle, he dropdown and access the edit page through the link
   </td>
   <td>When a logged in user clicks the ‘edit category’ link on the dropdown they are taken to the edit category page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Logged in User Category Delete Link
   </td>
   <td>If the user is logged in, they can toggle the dropdown and select the delete link to delete the post
   </td>
   <td>When a logged in user toggles the dropdown and clicks ‘delete category’ they are asked for confirmation before the category gets deleted
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Add Category Page


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Cancel Button
   </td>
   <td>When clicked, the button returns a user back to the page they came from
   </td>
   <td>The button returns a user to the correct page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Add Category Form Validation - Title
   </td>
   <td>The user cannot post the form with an empty title element
   </td>
   <td>The form will not post without a title and the user is directed to add one
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Add Category Form Validation - Description
   </td>
   <td>A user cannot post the form without a description entered  
   </td>
   <td>The form will not post without a description and the user is directed to add one
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Add Category Form, redirection
   </td>
   <td>When the user enters the form correctly they get redirected to the category list view, to see their new category
   </td>
   <td>When a satisfactory form is submitted, the user is redirected to the category list form 
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Add Tag


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Cancel Button
   </td>
   <td>When clicked, the button returns a user back to the page they came from
   </td>
   <td>The button returns a user to the correct page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Add Tag Form Validation
   </td>
   <td>The form cannot be posted without the entry of a valid title
   </td>
   <td>The form does not post and the user is prompted to enter a title
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Add Tag Form redirection 
   </td>
   <td>When the form is posted, the user is redirected back to the category list page
   </td>
   <td>When the form posts, the user is redirected to the category list page
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Logout Page 


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>The log out button
   </td>
   <td>When a logged in user clicks the logout button they are signed out and taken to the index page
   </td>
   <td>When a logged in user clicks the logout button they are logged out
   </td>
   <td>Pass
   </td>
  </tr>
</table>



### Login Page 


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Login Button
   </td>
   <td>When a user posts a correctly filled in form, they are redirected to the index page
   </td>
   <td>After logging in, a user is redirected to the index page
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Login Form- username field validation
   </td>
   <td>When a user tries to submit a form without a username, the form does not post and prompts them to correct this
   </td>
   <td>If a form is not entered correctly it does not post and the user is asked to resubmit
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Login form password field validation
   </td>
   <td>When a user tries to submit a form without a password, the form does not post and prompts them to correct this
   </td>
   <td>If a form is not entered correctly it does not post and the user is asked to resubmit
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Admin login button
   </td>
   <td>When a user clicks the admin login link, they are redirected to the admin login page
   </td>
   <td>When a user clicks the link they are taken to the admin login page
   </td>
   <td>Page
   </td>
  </tr>
</table>



### Sign Up


<table>
  <tr>
   <td>Feature
   </td>
   <td>Intended Outcome
   </td>
   <td>Actual Outcome
   </td>
   <td>Outcome
   </td>
  </tr>
  <tr>
   <td>Sign up form validation - Username
   </td>
   <td>A user cannot submit a form without entering a valid username 
   </td>
   <td>If a username is not entered, the form does not post and the must add a username before posting
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Sign up form validation - Password
   </td>
   <td>A user cannot submit a form without entering a valid password 
   </td>
   <td>A valid password must be entered before the form submits and the user will be prompted to enter a valid one
   </td>
   <td>pass
   </td>
  </tr>
  <tr>
   <td>Sign up form validation - Password
   </td>
   <td>A user cannot submit a form without entering the same password as they previously did
   </td>
   <td>If the incorrect password is entered, the user cannot post the form and must reenter their password
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>User redirection
   </td>
   <td>When a correctly entered form is submitted they are redirected to the index page 
   </td>
   <td>When a valid form is submitted they are redirected to the index page 
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Sign In link
   </td>
   <td>When a user clicks the login link, they are redirected to the login page
   </td>
   <td>When a user clicks the login link they are redirected to the correct page
   </td>
   <td>Pass
   </td>
  </tr>
</table>
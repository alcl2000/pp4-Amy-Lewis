# Testing document

-[Validators](#validators)
-[Manual Testing](#manual-testing)

## Validators

 -  All custom HTML pages on my site pass HTML validation from W3C 
 ![A screenshot showing the HTML validation from the W3C validator](static/assets/readme/html-validation-big.jpg)
 - My one page of CSS Passes validation from WC3 as well 
 ![A screenshot showing the CSS passing validation through the W3C validator](static/assets/readme/css-validation.jpg)
 - The Jquery file has passed validation through JShint
 ![A screenshot showing the JS file passing validtion from the JShint Jquery validator](static/assets/readme/jshint-validation.jpg)

 ### Python Validation
- All custom python files in the citizen_detective app pass python validation through CI's own pep8 validator
![The validation pass for admin.py](static/assets/readme/admin.py-validation.jpg)
![The validation pass for forms.py](static/assets/readme/forms.py-validation.jpg)
![The validation pass for models.py](static/assets/readme/models.py-validation.jpg)
![The validation pass for urls.py](static/assets/readme/urls.py-validation-cd.jpg)
- All the custom python files in the forum app pass python validation through CI's own pep8 validator
![The validation pass for urls.py](static/assets/readme/urls.py-validation-forum.jpg)
![The validation pass for views.py](static/assets/readme/views.py-testing.jpg)

## Manual Testing

### Index page 

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
 # Styx - Testing

[View the live project here.](https://styx-shoes.herokuapp.com/)


## Table of Contents

- [Styx - Testing](#styx---testing)
  - [Table of Contents](#table-of-contents)
  - [Code Validation](#code-validation)
  - [Validation Services](#validation-services)
  - [Validation of Code](#validation-of-code)
  - [Manual Testing](#manual-testing)
    - [Devices and browsers](#devices-and-browsers)
    - [Features tested](#features-tested)
  - [Bugs found and solved](#bugs-found-and-solved)


## Code Validation

## Validation Services

To validate the code the following **validation services** and **linters** were used to check the code:

* [W3C Markup Validator](https://validator.w3.org/)
    Checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, among others.

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    Checks the validity of cascading style sheets (css) and (X)HTML documents with style sheets.

* [PEP8 Online validation](http://pep8online.com/checkresult)
    This linter checks the validity of Python code against the PEP8 requirements

* [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)
    An open-source automated tool for improving webpages by running audits for performance, accessibility, progressive web apps, SEO etc.

    ![Lighthouse](/media/wireframes/lighthouse.png)


## Validation of Code 

|  Tested   | Link                                                      | Warning/Errors |
| :-------: | --------------------------------------------------------- | :------------: |
|   HTML    | [W3C Html validator](https://validator.w3.org/nu/)        |       No       |
|    CSS    | [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) |       No       |
| JavaScipt | [JSHint](https://jshint.com/)                             |       No       |
|  Python   | [PEP8](http://pep8online.com/)                            |       No       |

## Manual Testing

### Devices and browsers

**Browser versions used in testing:**

* Google Chrome Version 89.0.4389.114 (Official Build) (x86_64).
* Safari Version 14.0.3 (16610.4.3.1.7).
* Firefox Version 87.0 (64-bit)

**Tested on the following devices using the Google Chrome Developer tools:**

* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pr
* Surface Duo
* Galaxy Fold

**Tested on the following devices using the Firefox Developer tools:**

* Galaxy S9/S9+ Android 7.0
* iPad
* iPhone 6/7/8 iOS 11
* iPhone 6/7/8 plus iOS 11
* iPhone x/XS iOS 12
* Kindle Fire HDX Linux

**Tested on the following physical devices:**

* iPhone XS
* iPhone 12
* Samsung S20
* iPad Pro 12.9 2nd generation

### Features tested

**Notes about the testing performed:**
  * A super user and regular user account were created to test the elements only accessible to superusers stays hidden to regular users.
  * All buttons, forms and links were clicked and tested for responses, all form fields were filled out and responded as expected, all features were used and tested with appropriate responses given as a logged in user, superuser and unregistered user.
  * All buttons were tested by the developer to check that they responded correctly and displayed the correct information.
  * All links were tested by the developer to check they lead to the correct endpoints and gave the correct responses.
  * All items and their categories categories were tested by the developer to check that it responded correctly and displayed the correct information.
  * All forms were tested by the developer by filling them out using the wrong inputs to test validation and user feedback, which worked as expected. A red underline and text box appears alerting the user to the mistake.
  * Edit forms were tested by changing the  the information and viewing those changes on the pages affected. Edit forms were also already filled with the current information if the user chose to let their data to be stored. 
  * All 'Delete' buttons delete the appropriate information and take users back to the all products page, and explore page.
  * The back to top button takes the user to the top of the current page and has been tested and reponded as expected on every page.
  * Toasts give the user real time feed back on their inputs and are visiable with bold, clean text to grab the users attention. They show at the approprite time and with the correct text when diferent actions are performed.

**Home Page:**
  * Clicking the links on the image take users to the pages specified.
  * Clicking the links the shop dropdown take users to the product categories specified or the all products page if requested.
  * Clicking the Explore link takes users to the all blogs page.

**Search Bar:** 
* The search bar was tested by using not relevant search terms so it displayed 'No Results Found!', as expected, and the item count displays 0.
* The search bar generates results based on user input. Results are listed underneath. Words that are relevant to the site were searched all returning the correct information.
**Product Page:** 
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* Clicking the home button takes users to the main all products page.
* Clicking the product button takes the user to the sites main landing page, which has links to all other areas of the site, upon correct entry of their personal username and password, and the link to the 'Register' page transports the user to that page as expected.
* Clicking the forgot password button takes users through the process of setting a new password.

**Register Page:** 
* The form fields have validation, it was tested using correct and incorrect input, receiving the expected output. 
* Clicking the back to product and sign in links take the user back to the product page.
* Clicking the register button will trigger to send an email  to the used email address requesting to confirm their email address, will return to the main page. 

**All products - Dropdown** 
* All the links in the dropdown list take the user to the different categories avaiable in the page.
* The result of the users input is shown below with only the products listed in that category.
* The page displays a name header to show the user the category they are viweing, also an item count so they can see how many products are available in that category, next to a link that directs them to the all products page. The item count was tested by entering and removing products from the database and updates accordingly.
* The sort by dropdown is available for users to sort the products in the chosen category, it was tested by selecting all the availble sorting methods and observing the results, which were as expected.
* Both the product image and product name will take the user to that specific products details page.

**All products Page - Via Shop Link** 
* This link directs users to the all products page.
* The page displays an item count so users can see how many products there are in total. The item count was tested and updates when products are added and removed from the database.
* A sort by dropdown is available for users to sort the products in the page. The sort by was tested by clicking on every available method and observing the results visiable underneath.
The results were as expected on every method.
* Both the product image and product name take the user to that specific products details page.

**Product Detail page** 
* Show all the details of the selected product.
* A category link takes users to that products category, where they will find other products in that category if there are any in the database. It was tested by clicking on every available method.
* Users can use the amount minus and plus icons to select the amount of that product type to add to the bag. This has been tested with every product and the amount specified here will be added to the users shopping bag. 
* Superusers will find the Edit and Delete buttons as well. They are not visible to nonsuperusers and they were tested by creating a regular user.
* A continue shopping link directs users to the all products page whilst saving their current shopping bag.
* The add to bag button adds the specified amount of the specified product to the users shopping bag. Users are notified of the success of this or if there's been an error.

**Edit Product Button** 
* Only super users have access to this button (found on Product Details page), and it was tested by creating a regular user.
* Clicking the 'Edit' buttons take the user to a form with the fields filled out with the current information and the 'Edit' button in the forms changes the information in the database, before taking the user back to that products details page.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* The current image section shows a thumbnail of the current image with the option to remove it, select a new image from the files (select button) or add an image using the image url field.
All 3 methods were tested and behaved as expected.
* Clicking the 'Cancel' button will take the user back to the details page without making any changes, as expected.
* Users are notified of the successor if there is any errors so the request couldn't be processed.

**Product Management** 
* Only super users have access to this page (found in My Account dropdown), and it was tested by creating a regular user.
* Clicking the 'Add' buttons add the entered information to the database before taking the user back to the products details page.
* The form fields have validation, tested using correct and incorrect information with the expected responses given.
* Users can select a new image from the computers files via the select button or add an image using the image url field.
Both methods were tested and gave appropriate responses.
* Clicking the 'Cancel' buttons take the user back to their respective details page without making changes as expected.
* Users are notified of the success of this or if there's been an error.

**Explore page - Via Explore Nav Link** 
* The page has an item count so users can see how many blog posts there are in total. The item count was tested and behaves as expected when posts are added and removed from the database.
* Clicking the blog image or the name of the post take the user to the linked post page

**Explore Details** 
* Users must be logged in to use this feature. This was tested using a username of an user not logged in and was directed to the product page as expected.
* Superusers will find the Edit and Delete post buttons here. They are not visible to nonsuperusers and it was tested by creating a regular user.
* Clicking the back to blogs button directs users back to the all blogs page.
* The add a comment form is found under the blog post.
* The comments section has an item count so users can see how many comments there are on that post. The item count was tested and updates when comments are added and removed.
* Super users and the comment authors will find the edit and delete comment buttons under the comments. Superusers can delete posts by all users but if users aren't superusers they can only edit and delete their own comments. This was tested by creating posts by both superusers and 2 nonsuperusers and viewing the results, which were as expected.
* If a blog hasn't got any comments users will be informed via a 'No comments yet!' statement. This feature has been tested by adding a blog and not commenting.

**Edit Post Button** 
* Only super users have access to this button and it was tested by creating a regular user.
* Clicking the 'Edit' buttons take the user to a form with the fields filled out with the current information and the 'Edit' button in the forms changes updates the database, before taking the user back to that posts details page.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* The current image section shows a thumbnail of the current image with the option to remove it (checkbox), select a new image from the computers files (select button) or add an image using the image url field.
All 3 methods were tested and gave appropriate responses.
* Clicking the 'Cancel' buttons take the user back to that posts details page without making changes as expected.
* Users are notified of the success of this or if there's been an error.

**Explore Management** 
* Only super users have access to this page (found in My Account dropdown) and it was tested by creating a regular user.
* Clicking the 'Add' buttons add the entered information to the database before taking the user back to the posts details page.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* Users can select a new image from the computers files via the select button or add an image using the image url field.
Both methods were tested and gave appropriate responses.
* Clicking the 'Cancel' buttons take the user back to their respective details page without making changes as expected.
* Users are notified of the success of this or if there's been an error.

**Edit Comment Button** 
* Only super users and that comments author have access to this button.
* Superusers can delete comments by all users but if users aren't superusers they can only edit and delete their own comments.This was tested by creating comments by both superusers and 2 nonsuperusers and viewing the results, which were as expected.
* Clicking the 'Edit' buttons take the user to a form with the fields filled out with the current information and the 'Edit' button in the forms update the information in the database, before taking the user back to the main blog page.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* Clicking the 'Cancel' buttons take the user back to the main blog page without making changes es expected.
* Users are notified of the success of this or if there's been an error.

**Add Comment** 
* Users must be logged in to use this feature. Users who aren't logged in are directed to the product page and was tested using a user who wasn't logged in.
* Clicking the 'Add' buttons add the entered information to the database before refreshing the posts details page to show the added comment.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* Clicking the 'Cancel' button take the user back to the top of the posts details page without making changes as expected.
* Users are notified of the success of this or if there's been an error. 

**My Account Dropdown** 
* In 'My Account' dropdown, when logged in, shows relevant information depending on if it a superuser or no, with superusers getting the added management pages, alongside the profile and logout links. Tested both using superuser and nonsuperuser credentials.
* Using the 'My Account' dropdown users will be taken to the pages stated, with a confirmation of input required before logged them out via the logout button. Pressing cancel at this point takes users to the home page.
* Unregistered users and users not logged in will see product and register links. Tested using superuser and nonsuperuser credentials.

**Profile Page** 
  * The users username appears at the top as programmed with their email displayed underneath. This was tested using 3 users credentials with the correct information being displayed every time.
  * The profile page shows the users username and email address with a table containing their previous orders and current delivery information.
  * Clicking the order numbers, in the order history table, redirects users to a page with all the information available in that order. A reminder that the user is viewing an old order 
  is also displayed, with a link which takes users back to the profile page.
  * The current delivery information section has different fields that can be edited with updated information after clicking the update information button.
  If the user is logged in their information will automatically populate.
  The form has validation with explicit instructions when it's incorrect, tested with both correct and incorrect information with the expected results.
  * This page is only accessible if the user is logged in, it was tested using a username that wasn't logged in.

**Shopping bag** 
  * The Bag icon in the navbar takes the user to their shopping bag. There they will find a list of all the products added to it, as well as important information. If the bag is empty
  users will receive a notification in a toast, alongside a link which directs them to the all products page. This was tested by clicking the empty bag and clicking the bag with items inside and viewing the reults, which were as stated.
  * Users who have items in their bag will be faced with the option to update item amounts and delete items from their bag. Both the plus and minus buttons update the number in the box field, and the update and delete buttons update the subtotal, bag total, delivery and grand total to reflect the changes.
  If all the items are removed from the bag, users will be directed to a page stating that their bag is empty and a link which takes them to the all products page.
  * Clicking the continue shopping link directs users to the all products page.
  * Clicking the checkout button takes users to the checkout page where they find an order summary alongside an order form. 

**Checkout Page** 
  * All form fields work as intended and have validation in case the user doesn't fill the information in the correct format.
  The form was tested using correct and incorrect information, and gave the expected results and validation instructions.
  * Clicking the 'Save delivery info to profile' box, saves just the delivery sections users details to their profile page, which can be accessed via the 'My Account' dropdown. If the user has information saved to their profile, the delivery form fields will
  be automatically generated with the stored info. Any information changes made on this form update the info on the profile page when the save info box is checked.
  This was tested by changing the product information.
  * Clicking the bag link takes users back to their bag.
  * Clicking the checkout button generates the payment through stripe, adding the order to the admin section of the site and the users profile page. This was tested using multiple users and making orders then viewing the reults, which were as expected. 
  * The 'warning card is about to be debited' message updates with the bag user entries such as updating the amount of product and was tested by doing so.

**Thank You page** 
* When users have checked out and paid, they are directed to a thankyou page with a copy of their order and a link which directs the to the Latest Deals page. 
It will also display a toast message with all the details. 


**Subscription:** 
* The subscription form is available in all the pages. 
* It asks the user to input a correct email.
* User receives an email to confirm their subscription.
* A toast message displays showing:
  * Success - New user so they will have to check their email.
  * Info - If they have already subscribed.
  * Error - If there is an error. 

## Bugs found and solved

The issues found have been tracked on Github directly and can be found [here](https://github.com/CarolinaCobo/styx/issues?q=is%3Aissue+is%3Aclosed).

Inside each one of them there's information or screenshots showing what the error was and solved linking them to the commit where they were fixed. 


** To go back to [README.md](./README.md) **

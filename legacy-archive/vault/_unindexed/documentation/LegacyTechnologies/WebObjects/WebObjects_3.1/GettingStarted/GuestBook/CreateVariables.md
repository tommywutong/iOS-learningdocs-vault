---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/CreateVariables.html
archived_at: '2026-07-15T07:48:43.000023Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](CreateForms.md)

## Create variables

Now you have a form in which guests can enter information. You need to create variables that store this information. You need two variables: one to store the current guest's input, and another to store the list of all guests. You'll begin by declaring a class for these two variables.

### Create a class

The form you just created contains three pieces of information from a guest-name, e-mail, and comments. You could create three separate variables for these three pieces of information, but as you will see later, creating a class that has three attributes makes writing the application easier by allowing you to treat these three separate pieces as a single entity-a guest.
WebObjects Builder recognizes three types of classes: base classes, such as numbers and strings, composite classes, such as arrays and dictionaries, and custom classes. You don't need to do anything special to create variables of a base class or an array class. But if you want to create a dictionary, you must first go to the Classes window and define the dictionary.
In this task, you will create a dictionary class named Guest. The Guest dictionary class has three keys: name, email, and comments. (You can think of this dictionary as a C structure with three fields.)

- Go to the application window and click the Application tab.

The application object browser appears. You use this browser to declare variables that have an application-wide scope. These variables are declared in the application script, which is an optional part of a WebObjects application.

!- Choose Tools!Classes to display the Classes window. This window lists all of the classes that your application recognizes.
- Click the plus sign in the Classes table to create a new class.
- Name the class Guest. The Guest class is created with two default attributes.
- Rename the default attributes name and email.
- Click the plus sign in the Attribute table view to add a third attribute named comments.
- Close the Classes window.
!

As stated previously, Guest is a dictionary class. A dictionary contains key-value pairs. In the class definition you just created, you specified the keys (or attributes): name, email, and comments. When you create a variable of the Guest class, the variable will store values for each of these three keys.

### Declare variables

You just defined a Guest class so that you can store and manipulate guest information as a single entity. The next step is to create the array that will store the list of guests and a variable that will store the current guest information. As explained later, these variables are declared in two separate parts of the application: the list is declared in the application script, and the current guest is declared in the Main component.

- Go back to the application window and click the add variable button.
- Type __guests__ in the Name field and press Enter.
- Choose Guest from the Class pop-up list.
- Click the Array check box.

This creates the application variable __guests__, which is an array of Guests.

! .- Choose File!Save to save your changes to the application script.
- In the Main window, click the add variable button (in the bottom half of the screen).
- Name the variable __aGuest__ and select Guest from the Class pop-up list.
- Save the Main component.
!

### A closer look

You just created the variables that represent the current user's input (__aGuest__) and the list of all guests (__guests__).
You declared the __guests__ array in the application script (which is named __Application.wos__) instead of the Main component's script. Why? So that it would exist for the life of the application. If you declared __guests__ in the Main component (as you did the __aGuest__ variable), __guests__ would be created each time the Main page was redrawn. The Main page is redrawn every time a user clicks the Submit button, so __guests__ would only ever contain one item - the last user who clicked submit.
__Note:__ _Component variables_ exist only as long as the component does, which is up until that component's page needs to be redrawn. _Application variables_ (defined in __Application.wos__) live as long as the application does. There's a third type of variable, known as _session variables_. Session variables are declared in the session display of the application window and stored in the session script (__Session.wos__). They exist for the lifetime of one user's session. New session variables are created as new sessions are added. For example, if you declared a variable in __Session.wos__ and three users were using the application, three instances of that variable would be created, one for each user. If the first user changed the value of that variable, the other two users would not see the change because the session variable is unique to each user's session.
You can read more about application variable, session variables, and component variables in "[Using WebScript](../../DevGuide/WebScript/WebScript.mif.book.md)" in the _WebObjects Developer's Guide_.

[!Table of Contents](GuestBook.book.md) [!Next Section](BindElements.md)

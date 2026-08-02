---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/MainComponent.html
archived_at: '2026-07-15T07:48:16.964246Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](Application.md)

# Create the Main component

Now that you have a way to maintain and validate the list of registrants, it's time to create the user interface. Start by creating the __Main.wo__ component in WebObjects Builder.
This Main component is similar to the Main component you created in the GuestBook tutorial. It contains three input fields in which users enter information about themselves. There are two differences between this component and the component used in the GuestBook tutorial: This component contains a WOString dynamic element that displays a message indicating success or failure, and it has multiple submit buttons.

## Create the Main component's interface

- In WebObjects Builder, create a heading in the Main component window with the text "Register Now!"
- Create a form with two text fields and a multi-line text element like the one shown below. (See "Creating a Simple WebObjects Application" if you need help with this step.)
!- Create space below the multi-line text element, and then drag a WOString from the Abstract Elements palette.
!

## Create a dictionary class

As stated previously, the Registration application is similar to the GuestBook application from the first tutorial in this book. Like GuestBook, Registration keeps a list of people along with information about each person. In GuestBook, you represented the information about a given person as a dictionary, and you'll do the same in Registration. So just like you did with GuestBook, you have to define a dictionary class. You do this at the application level so that the class can be used in all of the application's components.

- In WebObjects Builder, go to Registration's application window.
- Click the Application tab.
- Choose Tools ! Classes to bring up the Classes window.
- Click the plus sign to create a new class.
- Name the class __aPerson__.
- Define three attributes for the aPerson class: name, email, and address.
- Set the class for each of these three attributes to be the String class.
- Close the Classes window.
!

## Create and bind variables

You have defined all of the component's interface elements. Now you need a way to bind the interface to the component's logic. You do this the same way whether you're using Java or WebScript-you add variables in the object browser and bind them to the component's dynamic elements.

- In the Main component window, create a variable of type aPerson. Name the variable __newPerson__.
!

This creates a dictionary variable __newPerson__ that has three attributes: name, email, and address.

- Select the text field labeled Name in the top part of the window.
- Bind the text field labeled Name to __newPerson__ ! __name__ by selecting the text field and double-clicking __newPerson__ ! __name__.

Double-clicking binds __newPerson__ ! __name__ to the Name text field's __value__ attribute.

!- Bind the text field labeled E-mail to __newPerson__ ! __email__.
- Bind the text area labeled Address to __newPerson__ ! __address__.

Now __newPerson__ is set up to contain the information from the Name, E-mail, and Address fields when the Submit button is clicked.

- Create another new variable, name it __message__, and set its class to String.
- Bind the WOString element to the __message__ variable.

This sets up the WOString to display a message indicating success or failure.

!

## Create multiple submit buttons

Now, create the form's buttons. The default form provides two buttons: a reset button and a submit button. You need an additional submit button, and you need to change the names of the existing buttons. You also need to set up the form so that it allows multiple submit buttons.

- Drag the cursor across the submit and reset buttons to select them. Click the left-align icon in the toolbar so that the buttons are no longer centered on the page.
!- Select the submit button.
- Double-click the word "Submit" inside the button.
- Type __Register__.
- Select the word "Reset" inside the reset button, and type __Clear__ in its place.
!- Place the cursor after the Clear button, and choose the menu command Format ! Form ! Add Submit Button to add another submit button.
- Select the word "Submit" inside the new submit button and type __Show All Registrants__ in its place.
- Select the entire form by clicking to the right of the String element or the multi-line text element.
- Click the inspector button to bring up the inspector panel.

The inspector panel's icon path contains two icons, one for the page's HTML attributes and one for the form's bindings.

!- Select the __multiplesubmit__ attribute, type the number 1 in the text field, and press Enter.
!

This binds the value 1 (or __true__) to the WOForm __multiplesubmit__ attribute, enabling multiple submit buttons in the form.

## Implement the methods

Now you need to define actions for the submit buttons.

- In the Main component window, click the Script button to display the Script window.

The Script window displays the __Main.java__ file. __Main.java__ defines your component, Main, to be a subclass of Component. __Main.java__ defines two instance variables and two methods. The instance variables are __newPerson__ and __message__, which you defined earlier using the object browser. The methods are __submit__ and __submit_2__. These methods were created automatically when you created the submit buttons.

- Change the name of the __submit__ method to __register__ and type this as its implementation:

```
    public Component register() {
        Person aPerson = new Person(newPerson);
        ImmutableHashtable results =
            ((Application)
            application()).manager().registerPerson(aPerson);

        if (((String)results.get("valid")).compareTo("No") == 0)
            message = ((String)(results.get("failureReason")));
        else
            message = "You have been succesfully registered.";
        return this;
    }
```


This method uses the two custom classes that you wrote earlier: Person and RegistrationManager. (Recall that Application's __manager__ method returns the RegistrationManager object.) The Person class's constructor creates an object that represents the current user. RegistrationManager's __registerPerson__ method verifies that the user has provided all necessary information, returning a dictionary that indicates two things: whether the information is valid and if not, the error message that should be displayed. If the information is not valid, the __message__ variable is set to the error message and is displayed by the WOString element. If the information is valid, the message "You have been successfully registered" is displayed.

- Change __submit_2__ to the __showRegistrants__ method shown below:

```
    public Component showRegistrants() {
        Component registrants =
            application().pageWithName("Registrants");
        return registrants;
    }
```


__showRegistrants__ returns the second page of the application, the page that displays the list of all who have registered.

- Add a constructor for the Main class.

```
    public Main() {
        super();
        if (newPerson == null) {
            newPerson = new MutableHashtable();
        }
        message = "";
    }
```

- Change __newPerson__'s declaration from Object to MutableHashtable.

When you created the __newPerson__ variable, you specified that its class was aPerson, which is a dictionary class. The dictionary can be one of two NeXT Java classes: ImmutableHashtable or MutableHashtable. WebObjects Builder isn't able to recognize custom dictionary classes, so it declared the variable as being of type Object rather than type MutableHashtable. The constructor you implemented in the previous step initializes the __newPerson__ variable to be an empty MutableHashtable, so you must make sure that __newPerson__'s declaration matches its initialization.

- Save the component and close the Script window.

## Bind the submit buttons

Now that you've implement the button actions, you need to bind the buttons to the actions.

- In the Main component window, select the Register button and double-click the __register__ method.

This binds the __action__ attribute of the button to the __register__ method, meaning that when the user clicks Register, the __register__ method is invoked.

- Select the Show All Registrants button and double-click the __showRegistrants__ method.
- Save the component.

You're through with the Main component, so you can close its window now.

[!Table of Contents](compiled.book.md) [!Next Section](Registrants.md)

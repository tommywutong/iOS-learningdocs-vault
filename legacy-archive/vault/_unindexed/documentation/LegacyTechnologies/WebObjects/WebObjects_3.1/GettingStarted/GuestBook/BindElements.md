---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/BindElements.html
archived_at: '2026-07-15T07:48:38.988335Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](CreateVariables.md)

## Bind the input elements

In the previous task, you created the application's variables. In the next task, you'll write a script that manipulates the variables. For the script to actually use the values of the dynamic HTML elements on the page, you first need to specify which variables represent which elements. This is called "binding" the elements.
There isn't a one-to-one correlation between dynamic elements and variables. Most dynamic elements have several attributes, and you bind each attribute to a different variable or method in your script. For example, WOTextField defines three attributes that define very different things: __value__ specifies the value the user enters in the text field, __name__ specifies a unique identifier for the text field, and __disabled__ specifies if the field is enabled or disabled. If you wanted non-default values for all three attributes, you'd bind them to three different variables.
To bind an element, you must specify three things:

- the variable (or method)
- the dynamic element
- the attribute within the dynamic element

WebObjects Builder provides a shortcut to creating bindings: you can select the variable, select the element, and let WebObjects Builder decide what attribute you want the variable bound to. Most of the time, the shortcut gives you the binding you want. This task shows you how to use the shortcut to bind the elements in the GuestBook.

- In the Main window, select the text field labeled Name in the GuestBook's form that you created earlier.
- In the object browser in the bottom half of the window, navigate to the __name__ attribute of __aGuest__.
- Double-click __name__.
!

This binds __aGuest.name__ to the __value__ attribute of the WOTextField labeled Name. After you perform this step, the text "aGuest.name" appears in the text field to show that it has been bound. A status message appears in the upper right corner of the editing display saying the binding has been made to WOTextField's __value__ attribute. This means that __aGuest.name__ represents the value entered in the Name field.

- Select the text field labeled E-mail and double-click __aGuest.email__ to bind it to the E-mail text field's __value__ attribute.
- Select the multi-line text element and double-click __aGuest.comments__ to bind it to the text element's __value__ attribute.

Unlike the text fields, the multi-line text element won't update to show you which variable it is bound to, but you will still receive the status message "bound to value."

- Save the Main component.

### A closer look

You just bound variables to dynamic elements in the HTML template. In the GuestBook application, the WOTextField and WOText elements are input fields-users will enter text in these fields, and the application will read the text. The bindings you made mean that after a user clicks Submit, __aGuest.name__ contains the value in the Name field, __aGuest.email__ contains the value in the E-mail field, and __aGuest.comments__ contains the value in the Comments field.!
At the beginning of this section, you learned that WOTextFields have three attributes: __value__, __name__, and __disabled__. Why didn't you have to make a binding to all three? Because __name__ and __disabled__ are optional attributes. If you don't bind variables to them, WebObjects assigns them default values. It creates a unique name to refer to the WOTextField, and it enables the text field by default. Later, you'll see an example of a dynamic element that has more than one variable bound to it.

[!Table of Contents](GuestBook.book.md) [!Next Section](ImplementMethod.md)

---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/ImplementMethod.html
archived_at: '2026-07-15T07:48:45.999620Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](BindElements.md)

## Implement a method

Now that you have declared some variables and you know which elements the variables represent, you need to write a script that uses this information. Specifically, the script needs to take the input from the form elements and add it to the end of the __guests__ array. You do this in the __submit__ method.
You may have noticed that when you dragged the form onto the page, the word "submit" appeared in the object browser at the bottom of the window. This represents the __submit__ method. When you create a form with a Submit button, WebObjects Builder creates a __submit__ method for you and binds the button to the method.

- In the Main window, click the script button to display a window containing Main's script file.

Main's script file appears in a separate window. It contains declarations for the variables and methods listed in Main's object browser, namely __aGuest__ and the __submit__ method. (You don't see the __guests__ array because it's declared in the application script, not the Main component.)

!- Enter the following line inside the declaration for the __submit__ method:

`[self.application.guests addObject:aGuest];`

- Close the script window and save the Main component.

### A closer look

You just implemented the __submit__ method. When the user clicks the Submit button, the variable __aGuest__ receives the values that the user entered in the form, and the __submit__ method is invoked. This method adds the information contained in __aGuest__ to the end of the application script's __guests__ array. The __guests__ array contains a list of everybody who ever used the GuestBook.
To implement this method, you used a language called WebScript. WebScript is the WebObjects scripting language. You can read more about it in "[Using WebScript](../../DevGuide/WebScript/WebScript.mif.book.md)" in the _WebObjects Developer's Guide_.

[!Table of Contents](GuestBook.book.md) [!Next Section](StaticHTML.md)

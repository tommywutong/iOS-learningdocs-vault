---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/AwakeSleep.html
archived_at: '2026-07-15T07:48:35.994708Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](BindAbstract.md)

# Implement awake and sleep

The final step to creating the GuestBook application is to implement the methods __awake__ and __sleep__. These two methods are standard methods that can be implemented in any component that needs them. __awake__ is a method that sets up the component at the beginning of every transaction. __sleep__ resets the component at the end of every transaction.

- Click the script button to display Main's script file.
- Add two more methods in the script window:

```
- awake {
    aGuest = [NSMutableDictionary dictionary];
}

- sleep {
    aGuest = nil;
}
```

- Choose File!Save All to save all of the files in the application.

You're done writing the GuestBook application, so you can exit WebObjects Builder.

## A closer look

The job of __awake__ is to prepare the page for the current transaction. In Main's case, whenever a new transaction begins, there's a new user to add to the guest list. Therefore, Main needs to allocate a new, empty __aGuest__ variable before the transaction begins. __aGuest__ (and all other variables of type Guest) are really NSMutableDictionary objects. NSMutableDictionary is a class defined in the Foundation Framework. NSMutableDictionary objects have key-value pairs. (The class is called "mutable" because you can change the contents of the dictionary after you create it.)
After the __awake__ method, WebObjects code takes the values from the form and assigns them to the attributes in the __aGuest__ variable. By the time the __submit__ method begins executing, __aGuest__ contains the current guest's information.
The __sleep__ method performs the inverse operation of the __awake__ method. It essentially erases any temporary state the page had for this transaction. Because you created an empty __aGuest__ variable in __awake__, you reset it to __nil__ in __sleep__.
The sequence of events for a transaction in the GuestBook goes like this:

- The user clicks the Submit button.
- Main's __awake__ method creates a new __aGuest__.
- WebObjects code populates __aGuest__'s attributes (name, e-mail, and comments) with information the user entered on the page.
- The __submit__ method adds __aGuest__ to the end of the guest list.
- The WORepetition iterates through the guest list and displays the name, e-mail, and comments of each guest.
- Main's __sleep__ method sets __aGuest__ to __nil__.

To learn more about __awake__, __sleep__, and WebScript in general, see "[Using WebScript](../../DevGuide/WebScript/WebScript.mif.book.md)" in the _WebObjects Developer's Guide_. To learn more about the Foundation Framework (where NSMutableDictionary is defined), see the [Foundation](../../DevGuide/Foundation/Foundation.book.md) chapter of the _WebObjects Developer's Guide_.

[!Table of Contents](GuestBook.book.md) [!Next Section](Run.md)

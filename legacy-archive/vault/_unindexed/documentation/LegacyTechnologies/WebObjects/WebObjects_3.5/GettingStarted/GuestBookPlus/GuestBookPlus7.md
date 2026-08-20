---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBookPlus/GuestBookPlus7.html
archived_at: '2026-07-15T07:54:01.661884Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookPlusTOC.md) [!Previous Section](GuestBookPlus6.md)

## Creating the Guest Object

Earlier in this chapter, you created a Java class of type Guest and wrote a constructor for it. You also added a variable of that class, __currentGuest__, to the Main component. However, adding a variable in this way doesn't actually create a new Guest object; you need to create one explicitly at some point in your code.
You'll create the Guest object in the constructor method for your component. This method is called when the component is first created; that is, the first time the user accesses the component.
__Note:__ In WebScript or Objective-C, you use a method called __init__ for this purpose.

- Choose View Source File from the pull-down menu at the bottom of the window.

Project Builder becomes active and displays the code for __Main.java__. Notice the following declaration that was added to your code when you added the __currentGuest__ variable:

```
protected Guest currentGuest;
```

- Delete the declarations of __guestName__, __email__ and __comments__, since you aren't using them anymore.
- Add the constructor method inside the Main class definition:

```
Main() {
        super();
        currentGuest = new Guest();
}
```


The first statement calls the constructor of Main's superclass (which is next.wo.Component). The second statement allocates a new empty Guest object and calls Guest's constructor to initialize its instance variables.

- Save __Main.java__.
- Build and run your application.

The application should work similarly to the first chapter, except that the guest's data is displayed in a table at the bottom of the page instead of as plain text.

!
At this point, your application still handles information from a single guest only; in the next section, you'll keep track of multiple guests.

[!Table of Contents](GuestBookPlusTOC.md) [!Next Section](GuestBookPlus8.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

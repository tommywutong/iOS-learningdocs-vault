---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.23.html
archived_at: '2026-07-15T08:07:23.695957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20the%20Finishing%20Touches.md) [!](Adding%20the%20Finishing%20Touches.md) [!](Adding%20a%20Dynamic%20Hyperlink.md)

---

#  Clearing the Guest List

While developing your application, you may find it useful to be able to remove all guests from the list. (Typically, you wouldn't allow users to remove all guests from the list.)

1. 

   In WebObjects Builder, make the GuestList component window active.
2. 

   Choose Add Action from the pull-down list at the bottom of the window. In the panel, enter clearGuestList as the name of the action and set the page returned to nil. Click Add.
3. 

   Choose View Source File from the pull-down list.

   Project Builder displays the code for __GuestList.wos__. __GuestList.wos__ is your script file, the WebScript equivalent of __Main.java__ in the Main component. You'll notice that there is a skeleton of the __clearGuestList__ action method, using WebScript syntax, as well as the declaration for __currentGuest__ that you created previously.
4. 

   Enter the following code before the return statement in __clearGuestList__:

   [[self application] clearGuests];

   This code calls the application's __clearGuests__ method, which removes all the Guest objects from the array.
5. 

   Save __GuestList.wos__ by choosing Save from the File menu.
6. 

   Go back to WebObjects Builder.
7. 

   Place the cursor below the table and press shift-Enter.
8. 

   Click ! to add a WOForm element to contain the button you'll create in the next step.
9. 

   Click !
   .

   This creates a submit button that the user will click to clear the guest list.
10. 

    Using the Inspector, double-click in the binding column next to the __value__ attribute and type "Clear Guest List".

    This changes the title of the button. Note that the quotes are necessary to indicate that you're binding a string, not a variable.
11. 

    Bind the __action__ attribute to __clearGuestList__.

    When the user clicks the button, the __clearGuestList__ action method is called, which causes the guest list to be cleared and the page to be redrawn.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20the%20Finishing%20Touches.md) [!](Adding%20the%20Finishing%20Touches.md) [!](Adding%20a%20Dynamic%20Hyperlink.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

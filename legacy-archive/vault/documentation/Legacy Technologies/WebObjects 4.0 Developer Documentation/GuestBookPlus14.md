---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBookPlus/GuestBookPlus14.html
archived_at: '2026-07-18T01:21:29.205123Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Enhancing%20Your%20Application.md) [!Previous Section](Adding%20the%20Finishing%20Touches.md)

## Clearing the Guest List

While developing your application, you may find it useful to be able to remove all guests from the list. (Typically, you wouldn't allow users to remove all guests from the list.)

- In WebObjects Builder, make the GuestList component window active.
- Choose Add Action from the pull-down menu at the bottom of the window. In the panel, enter clearGuestList as the name of the action and set the page returned to nil. Click Add.
- Choose View Source File from the pull-down menu.

Project Builder displays the code for __GuestList.wos__. __GuestList.wos__ is your script file, the WebScript equivalent of __Main.java__ in the Main component. For WebScript components, the script files are stored under the component, rather than in the Classes bucket. You'll notice that there is a skeleton of the __clearGuestList__ action method, using WebScript syntax, as well as the declaration for __currentGuest__ that you created previously.

- Enter the following code before the return statement in __clearGuestList__:

```
[[self application] clearGuests];
```


This code calls the application's __clearGuests__ method, which removes all the Guest objects from the array.

- Save __GuestList.wos__ by choosing Save from the File menu.
- Go back to WebObjects Builder.
- Place the cursor below the table and press Enter.
- Choose ! from the Elements pop-up list and click ! to add a WOForm element to contain the following button
- Click !.

This creates a submit button that the user will click to clear the guest list.

- Using the Inspector, bind the submit button's __value__ attribute to Clear Guest List.

This changes the title of the button. Note that the quotes are necessary to indicate that you're binding a string, not a variable.

- Bind the __action__ attribute to __clearGuestList__.

When the user clicks the button, the __clearGuestList__ action method is called, which causes the guest list to be cleared and the page to be redrawn.

[!Table of Contents](Enhancing%20Your%20Application.md) [!Next Section](GuestBookPlus15.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

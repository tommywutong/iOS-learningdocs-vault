---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBook/CreatingAppOutput.html
archived_at: '2026-07-18T01:20:49.785204Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Previous Section](ImplementActionMethod.md)

# Creating the Application's Output

So far, you have a way for the guest to enter information and a way for the application to store that information. Now, the application needs to do something with the information.
For now, you'll have the application simply display the same information the user entered, in a slightly different format. This allows you to verify that you have correctly received the data. To do this, you'll add dynamic string elements (WOStrings) to the main page and bind them. In the next chapter, you'll use more complex forms of output.

- In WebObjects Builder, place the cursor at the end of the document, making sure that it is _outside_the gray rectangle that represents the form, and press Enter.
- Choose ! from the Elements pop-up list to display the Structures buttons.
- Click ! to create a horizontal rule (an <HR> element).
- Press Enter to add a blank line.
- Select ! from the Elements pop-up list to display the Other WebObjects buttons.
- Add a WOString element by clicking !.

A WOString is a dynamic element whose value is determined at run time. It is shown as a small rectangle surrounded by two icons. !

- In the object browser, make a connection from the __guestName__ variable to the center rectangle of the WOString.

Notice that the name __guestName__ appears inside the WOString, and the Inspector panel doesn't come to the front. The message "Connected guestName to value" appears in the upper-right corner of the panel.

WebObjects provides this shortcut for binding to the __value__ attribute of WOStrings, because it is the attribute you most often want to bind. The __value__ attribute signifies the string that will be displayed when the page is drawn. If you want to bind a different attribute, you make a connection to the left or right icon, and the Inspector appears as usual.

- Click to the right of the WOString and press Enter.
- Create two more WOStrings and bind them to __email__ and __comments__, respectively.

Note that it isn't necessary to resize the WOStrings as you did with the text fields. They expand at run time to display the value of the variables to which they are bound.

- Save your component. It should now look like this:

!

In summary, when the user clicks the Submit button, a new request-response cycle begins. WebObjects stores the data entered in the dynamic form elements in the variables they are bound to (__guestName__ contains the value in the Name field, __email__ contains the value in the E-mail field, and __comments__ contains the value in the Comments field). It then triggers the action method bound to the __action__ attribute of the WOSubmitButton. The action method returns a page (which, in this example, is the same page). When the page is redrawn, the dynamic strings at the bottom show the values entered by the user.
Now you are ready to test your application.

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Next Section](Building%20and%20Running%20Your%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

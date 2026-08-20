---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.13.html
archived_at: '2026-07-15T08:07:03.834472Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20Simple%20WebObjects%20Application.md) [!](Implementing%20an%20Action%20Method.md) [!](Building%20and%20Running%20Your%20Application.md)

---

#  Creating the Application's Output

So far, you have a way for the guest to enter information and a way for the application to store that information. Now, the application needs to do something with the information.

For now, you'll have the application simply display the same information the user entered, in a slightly different format. This allows you to verify that you have correctly received the data. To do this, you'll add dynamic string elements (WOStrings) to the main page and bind them. In the next chapter, you'll use more complex forms of output.

1. 

   In WebObjects Builder, place the cursor at the end of the document, making sure that it is _outside_ the gray rectangle that represents the form, and press Shift-Enter.
2. 

   Click ! to create a horizontal rule (an <HR> element).
3. 

   Press Shift-Enter to add a blank line.
4. 

   Add a WOString element by clicking !
   .

   A WOString is a dynamic element whose value is determined at runtime. It is shown as a small rectangle surrounded by two icons. !
5. 

   In the object browser, make a connection from the __guestName__ variable to the center rectangle of the WOString.

Notice that the name __guestName__ appears inside the WOString, and the attribute pop-up menu doesn't appear. The message "Connected guestName to value" appears in the upper-right corner of the panel.

WebObjects provides this shortcut for binding to the __value__ attribute of WOStrings because it is the attribute you most often want to bind. The __value__ attribute signifies the string that will be displayed when the page is drawn. If you want to bind a different attribute, you make a connection to the left or right icon, and the attribute pop-up menu appears as usual.

6. 

   Click to the right of the WOString and press Shift-Enter.
7. 

   Create two more WOStrings and bind them to __email__ and __comments__, respectively.

Note that it isn't necessary to resize the WOStrings as you did with the text fields. They expand at runtime to display the value of the variables to which they are bound.

8. 

   Save your component. It should now look like this:
!

In summary, when the user clicks the Submit button, a new request-response cycle begins. WebObjects stores the data entered in the dynamic form elements in the variables they are bound to (__guestName__ contains the value in the Name field, __email__ contains the value in the E-mail field, and __comments__ contains the value in the Comments field). It then triggers the action method bound to the __action__ attribute of the WOSubmitButton. The action method returns a page (which, in this example, is the same page). When the page is redrawn, the dynamic strings at the bottom show the values entered by the user.

Now you are ready to test your application.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20a%20Simple%20WebObjects%20Application.md) [!](Implementing%20an%20Action%20Method.md) [!](Building%20and%20Running%20Your%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

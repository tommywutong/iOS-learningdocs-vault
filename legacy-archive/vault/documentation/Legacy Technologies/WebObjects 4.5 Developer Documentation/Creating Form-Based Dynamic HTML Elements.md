---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.d.html
archived_at: '2026-07-15T08:08:40.768470Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20the%20Page%27s%20Content.md) [!](Using%20the%20Inspector.md) [!](Resizing%20the%20Form%20Elements.md)

---

#  Creating Form-Based Dynamic HTML Elements

In this section, you'll create a form with several elements to capture input from a guest. The Submit and Reset buttons you add to the form will apply to all other elements in the form. These elements look and act like HTML form elements but are actually dynamic WebObjects elements, which enable your code to receive and manipulate the data entered by the user. Refer to the screen shot that follows these steps to see how the window should look.

1. 

   Place the cursor on the second line after the "My Guest Book" text.
2. 

   Click !
   .

   WebObjects Builder adds a form element to your component. The triangle at the upper-left corner indicates that it is a dynamic form, as opposed to a static form.The gray border indicates the extent of the form. You can increase its size by adding elements inside it.
3. 

   Type the text "Name: " and press Shift-Enter.

This text replaces the word "Form" that was displayed by default.

4. 

   Type "E-mail: " and press Shift-Enter twice.
5. 

   Type "Comments: " followed by Shift-Enter.

You have just entered three lines (and a blank line) of static text inside the form. Now you'll enter some dynamic elements to receive input from the user: two text fields and a multi-line text area.

6. 

   Place the cursor to the right of the text "Name: ".
7. 

   Click ! to create a dynamic text field element (WOTextField).
8. 

   Repeat steps 6 and 7 for "E-mail: ".
9. 

   Use the ! button to create a multi-line text area below the "Comments: " line.
10. 

    Press Shift-Enter twice to create two blank lines.
11. 

    Click ! to create a Submit button, which is used to send the data in the form to the server.
12. 

    Click ! to create a Reset button, which is used to clear the data in the form.

    The window should now look like this:

    !

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20the%20Page%27s%20Content.md) [!](Using%20the%20Inspector.md) [!](Resizing%20the%20Form%20Elements.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

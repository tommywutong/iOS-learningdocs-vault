---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook8.html
archived_at: '2026-07-15T07:53:33.488960Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBook7.md)

## Creating Form-Based Dynamic HTML Elements

In this section, you'll create a form with several elements to capture input from a guest. These elements look and act like HTML form elements but are actually dynamic WebObjects elements, which enable your code to receive and manipulate the data entered by the user.

- To display the dynamic form elements buttons in the toolbar, choose ! from the Elements pop-up list.
- Place the cursor on the line after the "My Guest Book" text and press Enter.
- Click !.

WebObjects Builder adds a form element to your component. The triangle at the upper-left corner indicates that it is a dynamic form, as opposed to a static form.The gray border indicates the extent of the form. You can increase its size by adding additional elements inside it.

- Type the text "Name: " and press Enter.

This text replaces the word "Form" that was displayed by default.

- Type "E-mail: " and press Enter twice
- Type "Comments: " followed by Enter.

You have just entered three lines (and a blank line) of static text inside the form. Now you'll enter some dynamic elements to receive input from the user: two text fields and a multi-line text area.

- Place the cursor to the right of the text "Name: ".
- Click ! to create a dynamic text field element (WOTextField).
- Repeat steps 7 and 8 for "E-mail: ".
- Use the ! button to create a multi-line text area below the "Comments: " line.
- Press Enter twice to create two blank lines.
- Click ! to create a Submit button, which is used to send the data in the form to the server.
- Click ! to create a Reset button, which is used to clear the data in the form.

The window should now look like this:

!

[!Table of Contents](GuestBookTOC.md) [!Next Section](GuestBook9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

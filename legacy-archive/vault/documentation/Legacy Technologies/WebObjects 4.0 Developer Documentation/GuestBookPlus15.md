---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBookPlus/GuestBookPlus15.html
archived_at: '2026-07-18T01:21:31.443513Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Enhancing%20Your%20Application.md) [!Previous Section](GuestBookPlus14.md)

## Adding a Dynamic Hyperlink

Now you'll create a hyperlink that returns the user to the Main page.

- Place the cursor below the submit button (outside the rectangle of its containing form).
- Choose ! from the Elements pop-up list and click !.
- Type Return to Sign-in Page, replacing the selected text.
- Inspect the hyperlink.
- Select the __pageName__ attribute, then double-click in the Binding column and type "Main" (including the quotes) .

__Note:__ You must specifically type the quotation marks in "Main", because you are specifying a string representing the name of the page to be returned. If you left off the quotes, you would be specifying a variable or method called __Main__.

- Save the GuestList component.
- Test your application.

__Note:__ In this case, you don't have to rebuild and relaunch your application in order to test it. Building is only required when you have made changes to Java or Objective-C code. If you modify a component or WebScript code only, the changes take effect even if the application is already running.

The GuestList page should now look like this:

!

[!Table of Contents](Enhancing%20Your%20Application.md) [!Next Section](Creating%20a%20WebObjects%20Database%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.24.html
archived_at: '2026-07-15T08:07:25.108354Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20the%20Finishing%20Touches.md) [!](Clearing%20the%20Guest%20List.md) [!](Creating%20a%20WebObjects%20Database%20Application.md)

---

#  Adding a Dynamic Hyperlink

Now you'll create a hyperlink that returns the user to the Main page.

1. 

   Place the cursor below the submit button (outside the rectangle of its containing form).
2. 

   Click !
   .
3. 

   Type Return to Sign-in Page, replacing the selected text.
4. 

   Inspect the hyperlink.
5. 

   Select the __pageName__ attribute, then double-click in the Binding column and type "Main" (including the quotes).

   __Note:__ You must specifically type the quotation marks in "Main", because you are specifying a string representing the name of the page to be returned. If you left off the quotes, you would be specifying a variable or method called __Main__.
6. 

   Save the GuestList component.
7. 

   Test your application. Since you didn't modify any Java or Objective-C code, you don't have to rebuild and relaunch your application.

   The GuestList page should now look like this:

   !

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20the%20Finishing%20Touches.md) [!](Clearing%20the%20Guest%20List.md) [!](Creating%20a%20WebObjects%20Database%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

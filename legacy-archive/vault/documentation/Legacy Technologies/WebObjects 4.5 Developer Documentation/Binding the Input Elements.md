---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.11.html
archived_at: '2026-07-15T08:07:01.900527Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Binding%20Elements.md) [!](Creating%20Variables.md) [!](Implementing%20an%20Action%20Method.md)

---

#   Binding the Input Elements

Each dynamic element contains several _attributes_. These attributes determine what happens when the element is displayed or when a form element is submitted. When you bind an element, you actually bind one or more of its attributes.

For example, a WOText element (which represents a multi-line text area) is defined as having two attributes:

- 

  __value__ specifies the string the user enters in the text area.
- 

  __name__ specifies a unique identifier for the text area.

In this tutorial, the only attribute you are concerned with is __value__, which represents the string entered by the user in the comments field. You'll bind this to the __comments__ variable. You don't need to bind the __name__ attribute in this application. In a later example, you'll bind more than one attribute of an element.

1. 

   In the object browser, make a connection by pressing on the __comments__ variable and holding down the mouse button while dragging to the Comments text area. Then release the mouse button.!

   A menu appears, displaying the attributes for the text area.
2. 

   Choose value.

   In the Dynamic Inspector, __comments__ appears in the Binding column next to the __value__ attribute of the text area, indicating that the binding has been made. Also, the text comments appears in the text field to show that it has been bound.
3. 

   We'll bind the __guestName__ variable using another technique. Select the Name WOTextField element. In the Inspector, select the Dynamic Inspector.

   The Inspector displays the __value__ attribute in red, indicating that this attribute must be bound; otherwise, WebObjects displays an error message when you try to run your application.
4. 

   In the Inspector, double-click in the Binding column next to __value__. Type g and press Enter. The Inspector fills in the rest of the "guestName" key for you.
5. 

   Bind the __email__ variable to the corresponding text field using one of the methods above.
6. 

   Save the Main component.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Binding%20Elements.md) [!](Creating%20Variables.md) [!](Implementing%20an%20Action%20Method.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

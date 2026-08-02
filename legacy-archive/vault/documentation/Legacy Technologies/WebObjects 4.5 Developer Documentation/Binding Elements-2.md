---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.48.html
archived_at: '2026-07-15T08:10:43.753008Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Creating%20a%20Detail%20Display%20Group-2.md) [!](Deleting%20Bindings.md)

---

#   Binding Elements

This section discusses the basic techniques you use to bind elements. Further detail is presented in the sections that discuss specific dynamic elements.

!

In the figure, you have added a form (WOForm) containing a dynamic text field (WOTextField) to your component. Note the triangle in the top left corner, which distinguishes the dynamic text field from a static HTML text field. The long rectangle surrounding the text field represents the containing form.

To bind the text field to the variable __myVar__
:

1. 

   Press mouse down on __myVar__
   in the object browser and drag to inside the text field.
   
   !

   A black line appears as you drag, and a black border appears around the text field, indicating that you can bind to it.
2. 

   Release the mouse button.

   A menu containing the attributes for that element appears.
3. 

   To complete the binding, click the attribute you want to bind (value in this case.)

   In the inspector, which you can access by clicking !
   in the toolbar, the name of the variable appears in the Binding column next to the attribute. Note that it also appears in blue inside the text field in the component window. Some (not all) dynamic elements display the binding for their default attribute inside the element itself.
   !

You can also bind an element's attributes by typing in the Inspector directly. To do this:

1. 

   Double-click in the binding column of the row for the attribute you want to set.
   
   !

   A cursor appears in the Binding column, allowing you to type.
2. 

   Type the binding in the text field. As you type, WebObjects Builder attempts to complete the binding using keys in the object browser.
3. 

   When the desired key appears in the binding column, press Enter.

When entering bindings this way, the following rules apply:

- 

  Constant strings (such as
  "Joe"
  ) must be in double quotes.
- 

  Variable and method names (such as joe
  ) must not be in quotes.
- 

  Symbolic constants (such as
  YES
  and
  NO
  ) must not be in quotes.
- 

  Keys must specify their full _key path_
  . For example, to bind the key that is selected in the following figure, you would type "a.a.c" to select
  application.allGuests.count
  .

!

#### [Deleting Bindings](Deleting%20Bindings.md#apple-obtwmslehuytiobqga)

#### [Other Binding Commands](Other%20Binding%20Commands.md#apple-obtwmslehuytiojvgi)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Creating%20a%20Detail%20Display%20Group-2.md) [!](Deleting%20Bindings.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

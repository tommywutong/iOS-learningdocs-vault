---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.18.html
archived_at: '2026-07-15T08:07:13.609612Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20Custom%20Guest%20Class.md) [!](Creating%20a%20Custom%20Guest%20Class.md) [!](Creating%20a%20Table%20to%20Display%20the%20Output.md)

---

#  Binding the Class's Instance Variables to the Form Elements

In the first chapter, you bound the input elements to variables in Main's code. Now you'll modify the bindings to use the class you just created.

1. 

   Select Web Components in the first column of the browser.
2. 

   Double-click __Main.wo__ in the second column of the browser to open the component in WebObjects Builder.
3. 

   Using the Add Key panel, add a variable called __currentGuest__ to your component and specify its type as Guest. (Note that you can now choose Guest from the Type combo box.)

   An entry for __currentGuest__ appears in the object browser. Notice the ">" symbol to the right of its name. This means that there is additional data to be displayed in the second column.
4. 

   Select __currentGuest__ in the object browser.

   The second column displays the three fields of __currentGuest__, as determined by the definition of its class, Guest.
5. 

   Make a connection from __guestName__ in the second column of the object browser (next to __currentGuest__) to the Name text field (press the mouse button down on the variable, drag to the element, and release the mouse button), and click __value__ in the pop-up menu.

   This time, when the pop-up menu appears, there is a dot next to the __value__ attribute because you bound it in the first tutorial.
6. 

   Bind the other two input elements to __currentGuest.email__ and __currentGuest.comments__.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20a%20Custom%20Guest%20Class.md) [!](Creating%20a%20Custom%20Guest%20Class.md) [!](Creating%20a%20Table%20to%20Display%20the%20Output.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

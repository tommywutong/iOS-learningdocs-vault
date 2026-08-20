---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.10.html
archived_at: '2026-07-15T08:07:00.627961Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Binding%20Elements.md) [!](Binding%20Elements.md) [!](Binding%20the%20Input%20Elements.md)

---

#  Creating Variables

In this section, you'll declare individual variables in your code file (__Main.java__) to hold the name, e-mail address, and comments entered by a single guest. Later on, you'll structure this information differently in order to work with data from multiple users.

WebObjects Builder allows you to declare variables without having to edit your source file directly. At the bottom of the panel there is a pull-down menu titled Edit Source. It has five items:

- 

  __Add Key__ allows you to add a _key_ to your source file. A key can be either an instance variable or a method that returns a value.
- 

  __Add Action__ allows you to add the template for an _action method,_ which is a method that takes no parameters and returns a component (the next page to be displayed).
- 

  __Delete Key__ allows you to delete a key from your source file by deleting the instance variable or the method that returns a value.
- 

  __Rename Key__ allows you to rename a key in your source file by renaming the instance variable or the method that returns a value.
- 

  __View Source File__ opens the source file in a Project Builder window.

1. 

   Choose Add Key from the pull-down menu.

   The Add Variable/Method panel opens.

   !
2. 

   Type guestName in the Name field.
3. 

   To specify the variable's type, select String from the combo box (or you can type String directly in the box).
4. 

   Click Add.

   You have just created a variable called __guestName__ of type String. It appears in the first column of the object browser. A declaration for __guestName__ also appears in __Main.java__, which you'll edit later.
5. 

   Create the variables __email__ and __comments__ in the same way (they are also of type String.)

__Note:__

You may also add variables by editing the source file in Project Builder. You will need to use Project Builder to remove or modify a variable. Remember to save the file after editing in Project Builder to update WebObjects Builder.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Binding%20Elements.md) [!](Binding%20Elements.md) [!](Binding%20the%20Input%20Elements.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

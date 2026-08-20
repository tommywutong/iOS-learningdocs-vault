---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook11.html
archived_at: '2026-07-15T07:53:18.016090Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBook10.md)

## Creating Variables

In this section, you'll declare individual variables in your code file (__Main.java__) to hold the name, e-mail address, and comments entered by a single guest. Later on, you'll structure this information differently in order to work with data from multiple users.
WebObjects Builder allows you to declare variables without having to edit your source file directly. At the bottom of the window there is a pull-down menu called Edit Main.java. It has three items:

- __Add Variable/Method__ allows you to add a _key_to your source file. A key can be either an instance variable or a method that returns a value.
- __Add Action__ allows you to add the template for an _action method_, which is a method that takes no parameters and returns a component (the next page to be displayed).
- __View Source File__ opens the source file in a Project Builder window.

- Choose Add Variable/Method from the pull-down menu.

The Add Variable/Method panel opens.

!- Type guestName in the Name field.
- To specify the variable's type, select String from the pop-up menu (or you can type String directly in the box.
- Click Add.

You have just created a variable called __guestName__ of type String. It appears in the first column of the object browser. A declaration for __guestName__ also appears in __Main.java__, which you'll edit later.

- Create the variables __email__ and __comments__ in the same way (they are also of type String.)

[!Table of Contents](GuestBookTOC.md) [!Next Section](GuestBook12.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

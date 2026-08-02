---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBook/CreatingVariables.html
archived_at: '2026-07-18T01:20:56.330240Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Previous Section](Binding%20Elements.md)

## Creating Variables

In this section, you'll declare individual variables in your code file (__Main.java__) to hold the name, e-mail address, and comments entered by a single guest. Later on, you'll structure this information differently in order to work with data from multiple users.
WebObjects Builder allows you to declare variables without having to edit your source file directly. At the bottom of the panel there is a pull-down menu titled Edit Main.java. It has three items:

- __Add Variable/Method__ allows you to add a _key_to your source file. A key can be either an instance variable or a method that returns a value.
- __Add Action__ allows you to add the template for an _action method_, which is a method that takes no parameters and returns a component (the next page to be displayed).
- __View Source File__ opens the source file in a Project Builder window.

- Choose Add Variable/Method from the pull-down menu.

The Add Variable/Method panel opens.

!

- Type guestName in the Name field.
- To specify the variable's type, select String from the pop-up menu (or you can type String directly in the box).
- Click Add.

You have just created a variable called __guestName__ of type String. It appears in the first column of the object browser. A declaration for __guestName__ also appears in __Main.java__, which you'll edit later.

- Create the variables __email__ and __comments__ in the same way (they are also of type String.)

__Note:__  You may also add variables by editing the source file in Project Builder. You will need to use Project Builder to remove or modify a variable. Remember to save the file after editing in Project Builder to update WebObjects Builder.

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Next Section](BindingInputElements.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

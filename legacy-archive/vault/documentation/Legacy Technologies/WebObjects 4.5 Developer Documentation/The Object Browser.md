---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.42.html
archived_at: '2026-07-15T08:10:35.616956Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Dragging%20Elements%20into%20the%20Component%20Window.md) [!](Working%20with%20Keys%20in%20WebObjects%20Builder.md)

---

#  The Object Browser

The bottom part of the component window is the _object browser_
, which displays your application's variables and methods. This display provides a graphical method of binding objects in your code to dynamic elements in the component.

!

The first column of the object browser displays two types of objects:

- 

  _Keys_
  are displayed above the horizontal line. A key can be either an instance variable or a method that returns a value.
- 

  _Actions_
  are displayed below the line. An action (or action method) is a method that takes no parameters and returns a component (the next page to be displayed).

A ">" next to an object's name in the browser indicates that it contains additional keys and actions, which are displayed in the next column when you select it.

In the figure, for example, the __application__
object is selected, showing that there are keys and actions defined in the application code. One of these, __allGuests__
, is an array (indicated by the ">>"), and the array's __count__
method is displayed in the next column.

__Note:__

If you rest the mouse pointer on a key, WebObjects Builder displays its type.

!

When you create a new project, the only keys that appear in the object browser are __application__
and __session__
(unless you use the Wizard to create a database application). These are methods that allow you to access variables in your application and session code.

!

There are several ways to add items to the object browser:

- 

  Use Project Builder to add keys and actions to your component's source file.

  When you save changes to a source file, WebObjects Builder parses the file, detects items that have been added and deleted, and updates the object browser's display to reflect the changes. The source code can be written in any of the languages that WebObjects supports (Java, Objective-C, or WebScript).
- 

  Use the menu at the bottom of the object browser to add items to your code directly from WebObjects Builder. See the next section, [Working with Keys in WebObjects Builder](Working%20with%20Keys%20in%20WebObjects%20Builder.md#apple-gi4tkmjt)
  , for more information.
- 

  Drag a _model file_
  , an entity from Enterprise Objects Modeler, or a relationship from Enterprise Objects Modeler into the browser to create a _display group_
  variable. See [Adding Display Groups](Adding%20Display%20Groups.md#apple-giztambr)
  for more information.

#### [Working with Keys in WebObjects Builder](Working%20with%20Keys%20in%20WebObjects%20Builder.md#apple-obtwmslehuytimzyhe)

#### [Working with Application and Session Variables](Working%20with%20Application%20and%20Session%20Variables.md#apple-obtwmslehuytimztgi)

#### [Adding Display Groups](Adding%20Display%20Groups.md#apple-obtwmslehuytimztg4)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Dragging%20Elements%20into%20the%20Component%20Window.md) [!](Working%20with%20Keys%20in%20WebObjects%20Builder.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

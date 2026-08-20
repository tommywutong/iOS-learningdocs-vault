---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements4.html
archived_at: '2026-07-18T01:25:59.928356Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Creating%20Dynamic%20Elements.md)

# The Object Browser

The bottom part of the component window is the _object browser_, which displays your application's variables and methods. This display provides a graphical method of binding objects in your code to dynamic elements in the component.

!

The first column of the object browser displays two types of objects:

- _Keys_ are displayed above the horizontal line. A key can be either an instance variable or a method that returns a value.
- _Actions_ are displayed below the line. An action (or action method) is a method that takes no parameters and returns a component (the next page to be displayed).

A ">" next to an object's name in the browser indicates that it contains additional keys and actions, which are displayed in the next column when you select it.
In the figure, for example, the __application__ object is selected, showing that there are keys and actions defined in the session code. One of these, __allGuests__, is an array (indicated by the ">>"), and the array's __count__ method is displayed in the next column.
__Note:__  If you rest the mouse pointer on a key, WebObjects Builder displays its type.
!
When you create a new project, the only keys that appear in the object browser are __application__ and __session__ (unless you use the Wizard to create a database application). These are methods that allow you to access variables in your application and session code_._

!

There are several ways to add items to the object browser:

- Use Project Builder to add keys and actions to your component's source file.

When you save changes to a source file, WebObjects Builder parses the file, detects items that have been added and deleted, and updates the object browser's display to reflect the changes. The source code can be written in any of the languages that WebObjects supports (Java, Objective-C, or WebScript).

- Use the menu at the bottom of the object browser to add items to your code directly from WebObjects Builder. See the next section, ["Creating Variables and Methods in WebObjects Builder"](DynamicElements5.md#apple-geytonbr), for more information.
- Drag a _model file_ into the browser to create a _display group_ variable. See ["Adding Display Groups"](DynamicElements6-2.md#apple-heyteni) for more information.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements5.md)

---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/ObjBrwsr.htm
archived_at: '2026-07-15T07:56:36.079869Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](CreateDE.md)

# The Object Browser

The bottom part of the component window is the _object browser_, which displays your application's variables and methods. This display provides a graphical method of binding objects in your code to dynamic elements in the component.!
The first column of the object browser displays two types of objects:

- _Keys_ are displayed above the horizontal line. A key can be either an instance variable or a method that returns a value.
- _Actions_ are displayed below the line. An action (or action method) is a method that takes no parameters and returns a component (the next page to be displayed).

A ">" next to an object's name in the browser indicates that it contains additional keys and actions, which are displayed in the next column when you select it.
In the figure, for example, the __session__ object is selected, showing that there are keys and actions defined in the session code. One of these, __selectedSailboards__, is an array (indicated by the ">>"), and the array's __count__ method is displayed in the next column.
Note that if you point to a key, WebObjects Builder displays its type.
!
When you create a new project, the only items that appear in the object browser are __application__ and __session__ (unless you use the Wizard to create a database application). These are methods that allow you to access variables in your application and session code_._!
There are several ways to add items to the object browser:

- Use Project Builder to add keys and actions to your component's source file.

When you save changes to a source file, WebObjects Builder parses the file, detects items that have been added and deleted, and updates the object browser's display to reflect the changes. The source code can be written in any of the languages that WebObjects supports (Java, Objective-C, or WebScript).

- Use the menu at the bottom of the object browser to add items to your code directly from WebObjects Builder. See the next section, ["Creating Variables and Methods in WebObjects Builder"](VarMeth.md#apple-geytonbr), for more information.
- Drag a _model file_ into the browser to create a _display group_ variable. See ["Adding Display Groups"](AddDspGp.md#apple-heyteni) for more information.

[!Table of Contents](DynElTOC.md) [!Next Section](VarMeth.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

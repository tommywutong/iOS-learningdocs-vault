---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.1f.html
archived_at: '2026-07-15T08:10:09.413988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](The%20Component%20Window.md) [!](Editing%20Views.md) [!](Selecting%20Elements%20in%20the%20Layout%20and%20Preview%20Views.md)

---

#  Source View

When you choose the source view, the text of your HTML template (_ComponentName_
__.html__
) appears. When you add elements in the layout view, their corresponding HTML tags appear in this file.

!

As you can see, when you begin with a blank page, WebObjects Builder automatically inserts the necessary elements such as <HTML>, <HEAD>, and <BODY> for you. The tags and text display in different colors according to their type: errors are red, markers are purple, comments are grey, WebObjects are blue, and text is black. You can change these colors using the Preferences panel. Choose Edit !
 Preferences (Edit !
 Options on Windows NT) to bring up the panel and click Syntax to set the syntax coloring preferences.

!

You select text elements as you would in most text-editing applications: by dragging, or by double-clicking words, or by Shift-clicking. The selected text appears shaded. When you triple-click on a tag, you select the tag, the matching tag, and the HTML in between. For example, if you triple-click on <TITLE> in a new page, WebObjects Builder selects <TITLE>, </TITLE>, and the "Page Title" text. You can also drag the mouse after you triple-click, which selects the matching tag and the HTML in between for the tag the mouse is on as you drag it.

The bottom pane of the source editing window shows your declarations (__Main.wod__
) file. When you bind variables and methods to your dynamic elements, this file stores the binding information. Normally, you don't edit this file directly. [Chapter 3](Dynamic%20Elements.md)
, [Working With Dynamic Elements](Dynamic%20Elements.md)
shows how you use WebObjects Builder to create bindings. Refer to the _WebObjects Developer's Guide_
for more information on working with the declarations file.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](The%20Component%20Window.md) [!](Editing%20Views.md) [!](Selecting%20Elements%20in%20the%20Layout%20and%20Preview%20Views.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/EdModes.htm
archived_at: '2026-07-15T07:57:00.481825Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](Toolbar.md)[Previous
Section](Toolbar.md) 

## Editing Modes

WebObjects Builder allows you to view and edit your
page in two modes:

- _Graphical mode_ shows a visual representation of your component,
  including its dynamic elements. The bottom pane, the object browser, lists
  the variables and methods that are defined in your scripts or code files. 
- _Source editing mode_ shows the text of your component's HTML template
  in the upper pane and the text of your declarations (__.wod__) file
  in the lower pane. In this mode, you can enter any HTML code. For example,
  you can include HTML elements that are not directly supported by WebObjects
  Builder's graphical tools.

The ! pop-up list at the left
of the toolbar allows you to switch between graphical editing mode and
source editing mode. When you choose source editing mode, the text of your
HTML template (_ComponentName___.html__) appears. When you add
elements graphically, their corresponding HTML tags appear in this file.

!

As you can see, when you begin with a blank page,
WebObjects Builder automatically inserts the necessary elements such as
<HTML>, <HEAD>, and <BODY> for you.

The bottom pane shows your declarations (__Main.wod__)
file. When you bind variables to your dynamic elements, this file stores
the information. Normally, you don't edit this file directly. ["Working
With Dynamic Elements"](../DynamicElements/DynElTOC.md#apple-gqytc) shows how you use WebObjects Builder to create
bindings. Refer to the _[WebObjects
Developer's Guide](../../DevGuide/DevGuideTOC.md)_ for more information on working with the declarations
file.

The Preferences panel provides several options
for how text is displayed in both graphical and source editing modes. Choose
Tools !Options to bring up the panel. For information
on resource-handling preferences, see ["Dragging
Elements into the Component Window"](../DynamicElements/CreateDE.md#apple-geydmnbq).

!

[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](EntText.md)[Next
Section](EntText.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

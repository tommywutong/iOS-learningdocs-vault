---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/Editing4.html
archived_at: '2026-07-18T01:27:17.117983Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](The%20WebObjects%20Builder%20Toolbar.md)

## Editing Modes

WebObjects Builder allows you to view and edit your page in two modes:

- _Graphical mode_ shows a visual representation of your component, including its dynamic elements. The bottom pane, called the object browser, lists the variables and methods that are defined in your scripts or code files.
- _Source editing mode_ shows the text of your component's HTML template in the upper pane and the text of your declarations (__.wod__) file in the lower pane. In this mode, you can enter any HTML code. For example, you can include HTML elements that are not directly supported by WebObjects Builder's graphical tools. You can also add components using the toolbar.

The ! pop-up list at the left of the toolbar allows you to switch between graphical editing mode and source editing mode. When you choose source editing mode, the text of your HTML template (_ComponentName___.html__) appears. When you add elements graphically, their corresponding HTML tags appear in this file.

!

As you can see, when you begin with a blank page, WebObjects Builder automatically inserts the necessary elements such as <HTML>, <HEAD>, and <BODY> for you.
The bottom pane shows your declarations (__Main.wod__) file. When you bind variables to your dynamic elements, this file stores the information. Normally, you don't edit this file directly. ["Working With Dynamic Elements"](Working%20With%20Dynamic%20Elements.md#apple-gqytc) shows how you use WebObjects Builder to create bindings. Refer to the [_WebObjects Developer's Guide_](The%20WebObjects%20Developer%27s%20Guide.md) for more information on working with the declarations file.

The Preferences panel provides several options for how text is displayed in both graphical and source editing modes. Choose Tools !Options to bring up the panel. For information on resource-handling preferences, see ["Dragging Elements into the Component Window"](Creating%20Dynamic%20Elements.md#apple-geydmnbq).!

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Editing5.md)

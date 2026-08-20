---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Reuse/SimpleInterface.html
archived_at: '2026-07-15T07:52:07.301547Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ReuseTOC.md) [!Previous Section](CentralResource.md)

## Simplifying Interfaces

Another benefit of reusable components is that they let you work at a higher level of abstraction than would be possible by working directly with HTML code or with WebObjects' dynamic elements. You (or someone else) can create a component that encapsulates a solution to a possibly complicated programming problem, and then reuse that solution again and again without having to be concerned with the details of its implementation. Examples of this kind of component include:

- A menu that posts different actions depending on the user's choice
- A calendar that lets a user specify start and end dates
- A table view that displays records returned by a database query

To illustrate this feature, consider a simple reusable component, an alert panel like the one shown in [Figure 28](#apple-he4tg).

!Figure 28. An Alert Panel
This panel is similar to the navigation table shown in [Figure 27](CentralResource.md#apple-giyti), but as you'll see, most of the component's attributes are customizable.

To use this component, you simply declare its position within the HTML page and give it a name:

```
    <HTML>
    <HEAD>
        <TITLE>Alert</TITLE>
    </HEAD>
    <BODY>

        <WEBOBJECT NAME = "ALERT"></WEBOBJECT>

    </BODY>
    </HTML>
```


The declarations file specifies the value for each of the panel's attributes, either by assigning a constant value or by binding the attributes value to a variable in the component's code (as with the __alertString__ and __infoString__ attributes here):

```
    ALERT: AlertPanel {
        alertString = alertTitle;
        alertFontColor = "#A00000";
        alertFontSize = 6;
        infoString = alertDescription;
        infoFontSize = 4;
        infoFontColor = "#500000";
        tableWidth = "50%";
    };
```


The component's code defines the __alertTitle__ and __alertDescription__ instance variables or methods, which set the text that's displayed in the upper and lower panes of the alert panel. The __alertDescription__ method could, for example, consult a database to determine the release date of the video.
WebObjects Builder makes working with reusable components such as AlertPanel even easier. Component clients can simply drag the alert panel into their components and use the Inspector to set the bindings. They don't need to manually edit the declarations file to set these bindings. To set this up, you, as the component creator, edit a file named __AlertPanel.api__ specifying both required and optional attributes. You could, for example, export only the __alertTitle__ and __infoString__ attributes (leaving the other attributes private) using this __AlertPanel.api__ file:

```
    Required = (alertTitle, infoString);
    Optional = ();
```


See the _WebObjects Tools and Techniques_ online book for more information.
AlertPanel is one of several components included in a sample application called ReusableComponents. This application demonstrates and documents how to create and use reusable components. If you look at the source code for AlertPanel, you'll notice that it's moderately complicated and, in fact, relies on other reusable components for its implementation. However, WebObjects lets you think of the AlertPanel component as a black box. You simply position the component in your HTML template, specify its attributes in the declarations file, and implement any associated dynamic behavior in your code.

[!Table of Contents](ReuseTOC.md) [!Next Section](Intercom.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

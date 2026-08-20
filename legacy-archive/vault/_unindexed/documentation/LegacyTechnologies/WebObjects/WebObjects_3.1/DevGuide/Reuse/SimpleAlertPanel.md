---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Reuse/SimpleAlertPanel.html
archived_at: '2026-07-15T07:47:22.843806Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Reuse.book.md)
[!Previous Section](SimpleInterface.md)

# A Simple Alert Panel

To illustrate how WebObjects can simplify interfaces to complex functionality, consider this reusable component, an alert panel:

!
 ____Figure 1.__  Alert Panel__

The panel is similar to the navigation table introduced above, but as you'll see, most of the component's attributes are customizable.

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

The declarations file specifies the value for each of the panel's attributes, either by assigning a constant value or by binding the attributes value to a value determined by the script file (as with the __alertString__ and __infoString__ attributes below):

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

The script file defines the __alertTitle__ and __alertDescription__ instance variables or methods (see "Intercomponent Communication" below for more information about binding attributes to methods), which set the text that's displayed in the upper and lower panes of the alert panel. The __alertDescription__ method could, for example, consult a database to determine the release date of the video.

WebObjects Builder makes working with reusable components such as AlertPanel even easier. For the component creator, WebObjects Builder lets you determine which of the reusable component's attributes will be "exported" to clients. You could, for example, export only the __alertTitle__ and __infoString__ attributes, but not allow clients to set font color, table width, and other attributes. Clients, on the other hand, can simply drag the AlertPanel from WebObjects Builder's palette window into their applications and use the Inspector to set the bindings. They don't need to manually edit the declarations file to set these bindings. See "Advanced WebObjects Builder Tasks" in the _WebObjects Builder Guide_ for more information.

AlertPanel is one of several components included in the Reusable Components Examples. If you take a look at the source code for AlertPanel, you'll notice that it's moderately complicated and in fact relies on other reusable components for its implementation. However, WebObjects lets you think of the AlertPanel component as a black box. You simply position the component in your HTML template, specify its attributes in the declarations file, and implement any associated dynamic behavior in the script file.

[!Table of Contents](Reuse.book.md)
[!Next Section](Intercom.md)

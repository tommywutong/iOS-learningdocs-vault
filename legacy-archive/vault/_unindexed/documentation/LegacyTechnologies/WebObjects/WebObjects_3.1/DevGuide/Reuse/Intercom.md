---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Reuse/Intercom.html
archived_at: '2026-07-15T07:47:19.401299Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Reuse.book.md)
[!Previous Section](SimpleAlertPanel.md)

# Intercomponent Communication

Reusable components can vary widely in scope, from as extensive as an entire HTML page to as limited as a single character or graphic in a page. They can even serve as building blocks for other reusable components. When a reusable component is nested within another component, be it a page or something smaller, the containing component is known as the _parent component_, and the contained component is known as the _child component_. This section examines the interaction between parent and child components.

In the AlertPanel example above, you saw how the parent component, in its declarations file, sets the attributes of the child component:

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

Each of the AlertPanel's attributes is set either statically (for example, alertFontSize = 6) or dynamically, by binding the attribute's value to a variable or method invocation in the parent's script file (for example, `alertString = alertTitle`). Communication from the parent to the child is quite straightforward.

But for reusable components to be truly versatile, there must also be a mechanism for the child component to interact with the parent, either by setting the parent's variables or invoking its methods, or both. This mechanism must be flexible enough that a given child component can be reused by various parent components without having to be modified in any way. WebObjects provides just such a mechanism, as illustrated by the following example.

[!Table of Contents](Reuse.book.md)
[!Next Section](AlertPanelWithResponse.md)

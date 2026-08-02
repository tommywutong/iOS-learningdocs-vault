---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/Integrating1.html
archived_at: '2026-07-15T07:46:36.671674Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](Integrating0.md)

## __1. Place dynamic-element markers (WEBOBJECT) in the HTML file__

You position and identify applet controls as dynamic elements in the HTML file of the component (page) just as you do any other dynamic element.

```swift
    <!-- Other HTML goes here -->
    Enter a string in the field, select a function from the list and press the Do It button:
    <br>
    <WEBOBJECT name=INPUTFIELD></WEBOBJECT>
    <WEBOBJECT name=FUNCTION></WEBOBJECT>
    <br>
    <WEBOBJECT name=BUTTON></WEBOBJECT>
    <br>
    Result:
    <br>
    <WEBOBJECT name=OUTPUTFIELD></WEBOBJECT>
    <br>
    <!-- Other HTML goes here -->
```

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](Integrating2.md)

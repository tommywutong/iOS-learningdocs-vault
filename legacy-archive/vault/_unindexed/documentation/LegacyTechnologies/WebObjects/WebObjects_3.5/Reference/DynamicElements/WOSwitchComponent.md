---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOSwitchComponent.html
archived_at: '2026-07-15T07:55:36.481770Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOSubmitButton.md)

## WOSwitchComponent

### Synopsis

__WOSwitchComponent {__ __WOComponentName__=_aComponentName___;__ ... __};__

### Description

WOSwitchComponent provides a way to determine at runtime which nested component should be displayed. This component is useful when you want to decide how to display information based on the state of the application.

**__WOComponentName__**
: Name of the component to display. This attribute can be a string or a method that returns the name of a component.

If the component specified in __WOComponentName__ takes attributes, pass these attributes along to WOSwitchComponent following the __WOComponentName__ attribute. Note that this means that all components that can be displayed by this WOSwitchComponent must use the same API.

### Examples

[Dynamically deciding which component to use](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=SwitchComponentEx)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOText.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

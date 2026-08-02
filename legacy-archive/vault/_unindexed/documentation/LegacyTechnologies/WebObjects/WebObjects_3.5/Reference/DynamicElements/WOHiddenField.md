---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOHiddenField.html
archived_at: '2026-07-15T07:55:26.781868Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOGenericElement.md)

## WOHiddenField

### Synopsis

__WOHiddenField__ __{__ __value__=_defaultValue___;__ [ __name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

A WOHiddenField adds hidden text to the HTML page. It corresponds to the HTML element <INPUT TYPE="HIDDEN"...>. Hidden fields are sometimes used to store application state data in the HTML page. In WebObjects, the WOStateStorage element is designed expressly for this purpose.

**__value__**
: Value for the hidden text field.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, the element appears in the page but is not active.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOHyperlink.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

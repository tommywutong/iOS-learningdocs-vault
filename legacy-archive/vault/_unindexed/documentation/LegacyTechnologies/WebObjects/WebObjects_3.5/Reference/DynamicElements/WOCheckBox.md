---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOCheckBox.html
archived_at: '2026-07-15T07:55:22.837013Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOBrowser.md)

## WOCheckBox

### Synopsis

__WOCheckBox__ __{value__=_defaultValue___;__ [__selection__=_selectedValue___;__] [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__
__WOCheckBox__ __{checked__=YES|NO__;__ [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

A WOCheckBox object displays itself in the HTML page as its namesake, a check box user interface control. It corresponds to the HTML element <INPUT TYPE="CHECKBOX"...>.
If you want to create a list of check boxes, use [WOCheckBoxList](WOCheckBoxList.md) in the WOExtensions framework instead of this element.

**__value__**
: Value of this input element. If not specified, WebObjects provides a default value.

**__selection__**
: If __selection__ and __value__ are equal when the page is generated, the check box is checked. When the page is submitted, __selection__ is assigned the value of the check box.

**__checked__**
: During page generation, if __checked__ evaluates to YES, the check box appears in the checked state. During request handling, checked reflects the state the user left the check box in: YES if checked; NO if not.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, this element appears in the page but is not active. That is, __selection__ won't contain the user's selection when the page is submitted.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOConditional.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

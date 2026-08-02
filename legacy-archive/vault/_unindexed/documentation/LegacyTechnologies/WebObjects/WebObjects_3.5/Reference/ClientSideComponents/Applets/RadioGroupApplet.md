---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/ClientSideComponents/Applets/RadioGroupApplet.html
archived_at: '2026-07-15T07:55:13.461502Z'
---
> 导航：[总目录](../../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CSControls.mif.book.md)
[!Previous Section](ListApplet.md)

---

# __RadioGroupApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.RadioGroupApplet.class";

__iitemList__=_anArray_; __selectedItem__=_itemIndex_; __action__=_method_;...};

### Description

A RadioGroupApplet is a control for mutually exclusive choices. It is a vertical matrix of check boxes (see CheckboxApplet) of which only one box can be checked at a time. The RadioGroupApplet class "wraps" the __java.awt.CheckboxGroup__ class.

**__iitemList__**
: An array of strings for the titles of the radio buttons.

**__selectedItem__**
: Numeric index of the check box selected in __itemList__. Index 0 identifies the first item in the array.

**__action__**
: The method invoked when a choice is made.

[!Table of Contents](CSControls.mif.book.md)
[!Next Section](ScrollingTextApplet.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

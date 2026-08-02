---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/ClientSideComponents/Applets/CheckboxApplet.html
archived_at: '2026-07-15T07:55:11.524861Z'
---
> 导航：[总目录](../../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CSControls.mif.book.md)
[!Previous Section](ButtonApplet.md)

---

# __CheckboxApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.CheckboxApplet.class";

__title__=_aTitle_; __action__=_method_; __checked__="YES"|"NO";...};

### Description

A CheckboxApplet is a control that uses an image of a check box to indicate "off" and "on" (or unselected and selected) states. It can invoke an action method upon a change of state. The CheckboxApplet class "wraps" the __java.awt.Checkbox__ class.

**__title__**
: The title of the check box.

**__action__**
: The method to invoke when the check box is clicked.

**__checked__**
: During page generation, if __checked__ evaluates to "YES", the check box appears in the checked state. In each subsequent synchronization point, __checked__ reflects the state the user left the check box in and the state it's set to by the action method.

[!Table of Contents](CSControls.mif.book.md)
[!Next Section](ChoiceApplet.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

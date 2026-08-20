---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTextField.html
archived_at: '2026-07-15T08:11:45.130607Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTextField

> **__Inherits
> from:__**
> : javax.swing.JTextField :
> javax.swing.JTextComponent :
> javax.swing.JComponent :
> java.awt.Container :
> java.awt.Component :
> Object

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOTextField is a subclass of javax.swing.JTextField
that adds the notion of _selectability._

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

When an EOTextField object is selectable, it behaves in every
way as a JTextField. However, when an EOTextField is not selectable,
its text can't be selected. An EOTextField is selectable by default.
To set it so it's not selectable, invoke [setSelectable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbponsxiu3fnrswg5dbmjwgk) with `false`.

## Instance Methods

---

### isFocusTraversable

`public boolean isFocusTraversable()`

Returns the result of the `super`'s
implementation if the receiver is selectable, `false` otherwise.

---

### setSelectable

`public void setSelectable(boolean  flag)`

Sets the receiver as selectable
if  _flag_ is true, or as unselectable
otherwise.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

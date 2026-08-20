---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOTextField.html
archived_at: '2026-07-15T08:13:54.800358Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOTextField

> **__Inherits from:__**
> : javax.swing.JTextField : javax.swing.text.JTextComponent : javax.swing.JComponent : java.awt.Container : java.awt.Component : Object

> **__Implements:__**
> : javax.swing.SwingConstants: javax.swing.Scrollable: javax.accessibility.Accessible: java.io.Serializable: java.awt.image.ImageObserver: java.awt.MenuContainer

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

EOTextField is a subclass of javax.swing.JTextField that adds the notion of _selectability_.

When an EOTextField object is selectable, it behaves in every way as a JTextField. However, when an EOTextField is not selectable, its text can't be selected. An EOTextField is selectable by default. To set it so it's not selectable, invoke [setSelectable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbponsxiu3fnrswg5dbmjwgk) with `false`..

## Interfaces Implemented

---

> : javax.swing.SwingConstants:
>
> : javax.swing.Scrollable:
>
> : javax.accessibility.Accessible:
>
> : java.io.Serializable:
>
> : java.awt.image.ImageObserver:
>
> : java.awt.MenuContainer:

## Method Types

---

> **All methods**
>
> : [EOTextField](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbpivhvizlyordgszlmmq): [isFocusTraversable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbpnfzum33dovzvi4tbozsxe43bmjwgk): [isSelectable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbpnfzvgzlmmvrxiylcnrsq): [processMouseEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbpobzg6y3fonzu233vonsuk5tfnz2a): [processMouseMotionEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbpobzg6y3fonzu233vonsu233unfxw4rlwmvxhi): [setSelectable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cgnfswyzbponsxiu3fnrswg5dbmjwgk)

## Constructors

---

### EOTextField

`public EOTextField()`

Description forthcoming.

---

## Instance Methods

---

### isFocusTraversable

`public boolean isFocusTraversable()`

Returns the result of the `super`'s implementation if the receiver is selectable, `false` otherwise.

---

### isSelectable

`public boolean isSelectable()`

Description forthcoming.

---

### processMouseEvent

`protected void processMouseEvent(java.awt.event.MouseEvent aMouseEvent)`

Description forthcoming.

---

### processMouseMotionEvent

`protected void processMouseMotionEvent(java.awt.event.MouseEvent aMouseEvent)`

Description forthcoming.

---

### setSelectable

`public void setSelectable(boolean flag)`

Sets the receiver as selectable if _flag_ is true, or as unselectable otherwise.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

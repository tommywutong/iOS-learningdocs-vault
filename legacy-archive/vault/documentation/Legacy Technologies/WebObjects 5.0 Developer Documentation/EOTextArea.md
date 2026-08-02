---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOTextArea.html
archived_at: '2026-07-15T08:13:54.766958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOTextArea

> **__Inherits from:__**
> : javax.swing.JScrollPane : javax.swing.JComponent : java.awt.Container : java.awt.Component : Object

> **__Implements:__**
> : EOTextComponentAccess: java.io.Serializable: java.awt.image.ImageObserver: java.awt.MenuContainer

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

EOTextArea, a subclass of javax.swing.JScrollPane, is used to represent scrolling text regions. An EOTextArea object uses a JTextArea to do its work. The main business of an EOTextArea is to configure the JTextArea's behavior and appearance. An EOTextArea's JTextArea has a vertical scroll bar but not a horizontal scroll bar and it wraps its lines of text. If you want to perform additional configuration on an EOTextArea's JTextArea, you can access the JTextArea with the method [textArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3umv4hiqlsmvqq).

## Interfaces Implemented

---

> : EOTextComponentAccess
>
> : [textComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3umv4hiq3pnvyg63tfnz2a)
>
> :
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
> : [EOTextArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl2fj5kgk6duifzgkyi): [setEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2ekzdjorqwe3df): [setOpaque](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2e64dbof2wk): [setSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2fg2l2mu): [setSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2fg2l2mu): [setText](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2fizlyoq): [textArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3umv4hiqlsmvqq)

## Constructors

---

### EOTextArea

`public EOTextArea()`

Description forthcoming.

---

## Instance Methods

---

### setEditable

`public void setEditable(boolean flag)`

Sets the receiver's editability (by setting its JTextArea's editability).

---

### setOpaque

`public void setOpaque(boolean flag)`

Sets whether or not the receiver is opaque (by setting its JTextArea to be opaque or not).

---

### setSize

`public void setSize(java.awt.Dimension aDimension)`

Sets the size of the receiver's JTextArea to _aDimension_ , and then resizes the text area to accommodate the vertical scroll bar.

---

### setSize

`public void setSize( int width, int height)`

Sets the size of the receiver's JTextArea to _width_ and _height_, and then resizes the text area to accomodate the vertical scroll bar.

---

### setText

`public void setText(String text)`

Sets the text of the receiv'ers JTextArea to _text_.

---

### textArea

`public javax.swing.JTextArea textArea()`

Returns the receiver's JTextArea.

---

### textComponent

`public javax.swing.text.JTextComponent textComponent()`

Returns the receiver's JTextArea.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

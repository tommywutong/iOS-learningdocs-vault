---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTextArea.html
archived_at: '2026-07-15T08:11:45.079758Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTextArea

> **__Inherits
> from:__**
> : javax.swing.JScrollPane :
> javax.swing.JComponent :
> java.awt.Container :
> java.awt.Component :
> Object

> **__Implements:__**
> : EOTextAssociation.JTextComponentAccess

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOTextArea, a subclass of javax.swing.JScrollPane,
is used to represent scrolling text regions. An EOTextArea object
uses a JTextArea to do its work. The main business of an EOTextArea
is to configure the JTextArea's behavior and appearance. An EOTextArea's
JTextArea has a vertical scroll bar but not a horizontal scroll
bar and it wraps its lines of text. If you want to perform additional
configuration on an EOTextArea's JTextArea, you can access the
JTextArea with the method [jTextArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3kkrsxq5cbojswc).

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

## Interfaces Implemented

---

> EOTextAssociation.JTextComponentAccess: [jTextComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3kkrsxq5cdn5wxa33omvxhi)

## Method Types

---

> **Accessing the text area's
> JTextArea**
> : [jTextArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3kkrsxq5cbojswc)
>
> **Methods forwarded to
> the text area's JTextArea**
> : [setEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2ekzdjorqwe3df)
> : [setOpaque](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2e64dbof2wk)
> : [setSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2fg2l2mu)
> : [setText](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbojswcl3tmv2fizlyoq)

## Instance Methods

---

### jTextArea

`public javax.swing.JTextArea jTextArea()`

Returns the receiver's JTextArea.

---

### jTextComponent

`public javax.swing.text.JTextComponent jTextComponent()`

Returns the receiver's JTextArea.

---

### setEditable

`public void setEditable(boolean  flag)`

Sets the receiver's editability
(by setting its JTextArea's editability).

---

### setOpaque

`public void setOpaque(boolean  flag)`

Sets whether or not the receiver
is opaque (by setting its JTextArea to be opaque or not).

---

### setSize

`public void setSize(java.awt.Dimension  aDimension)`

`public void setSize(int  width, int  height)`

Sets the size of the receiver's
JTextArea to  _aDimension_ or to  _width_ and  _height,_
and then resizes the text area to accommodate the vertical scroll
bar.

---

### setText

`public void setText(String  aString)`

Sets the receiver's text
value to  _aString_ by setting the receiver's
JTextArea's text.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

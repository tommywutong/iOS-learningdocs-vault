---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOMatrix.html
archived_at: '2026-07-15T08:13:54.513089Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOMatrix

> **__Inherits from:__**
> : [EOView](EOView.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvm2lfo4) : javax.swing.JPanel : javax.swing.JComponent : java.awt.Container : java.awt.Component : Object

> **__Implements:__**
> : java.awt.LayoutManager: NSDisposable: javax.accessibility.Accessible: java.io.Serializable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

EOMatrix is a class used to group collections of mutually exclusive JRadioButtons and to lay them out on a grid. It is a subclass of EOView that uses a java.awt.GridLayout.

For more information on the way a matrix of JRadioButtons behaves, see the Sun class documentation for javax.swing.ButtonGroup.

## Interfaces Implemented

---

> : java.awt.LayoutManager:
>
> : NSDisposable:
>
> : javax.accessibility.Accessible:
>
> : java.io.Serializable:

## Method Types

---

> **All methods**
>
> : [EOMatrix](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxi4tjpaxukt2nmf2he2ly): [add](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvqxi4tjpaxwczde)

## Constructors

---

### EOMatrix

`public EOMatrix( int rows, int columns, int rowSpacing, int columnSpacing)`

Description forthcoming.

---

## Instance Methods

---

### add

`public java.awt.Component add(java.awt.Component radioButton)`

Adds _radioButton_ if it's an instance of javax.swing.JRadioButton, otherwise simply returns.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

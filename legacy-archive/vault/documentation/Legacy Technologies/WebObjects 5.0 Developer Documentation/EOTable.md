---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOTable.html
archived_at: '2026-07-15T08:13:54.750986Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOTable

> **__Inherits from:__**
> : javax.swing.JScrollPane : javax.swing.JComponent : java.awt.Container : java.awt.Component : Object

> **__Implements:__**
> : NSDisposable: java.io.Serializable: java.awt.image.ImageObserver: java.awt.MenuContainer

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

The EOTable class is used to represent tables of data. An EOTable object uses a JTable to do its work. As a subclass of JScrollPane, an EOTable wraps its JTable in a scroll view and adds the JTable's JTableHeader to the EOTable's column header. If you want to configure or message an EOTable's JTable, you can access the it with the method [table](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dff52gcytmmu)..

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dff5sgs43qn5zwk)
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
> : [EOTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dff5cu6vdbmjwgk): [table](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dff52gcytmmu)

## Constructors

---

### EOTable

`public EOTable()`

Description forthcoming,

---

## Instance Methods

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

---

### table

`public javax.swing.JTable table()`

Returns the receiver's JTable.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

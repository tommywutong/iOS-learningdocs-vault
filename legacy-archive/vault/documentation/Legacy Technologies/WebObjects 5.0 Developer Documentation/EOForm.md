---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOForm.html
archived_at: '2026-07-15T08:13:54.452535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOForm

> **__Inherits from:__**
> : [EOMatrix](EOMatrix.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu2yluojuxq) : [EOView](EOView.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvm2lfo4) : javax.swing.JPanel : javax.swing.JComponent : java.awt.Container : java.awt.Component : Object

> **__Implements:__**
> : java.awt.LayoutManager: NSDisposable: javax.accessibility.Accessible: java.io.Serializable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

The EOForm class is a subclass of EOMatrix that manages a collection of titled text fields laid out on a grid. Each title/text field pair is an EOFormCell.

## Interfaces Implemented

---

> : java.awt.LayoutManager
>
> : [addLayoutComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3jpmfsgitdbpfxxk5cdn5wxa33omvxhi): [layoutContainer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3jpnrqxs33vorbw63tumfuw4zls): [minimumLayoutSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3jpnvuw42lnovwuyylzn52xiu3jpjsq): [preferredLayoutSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3jpobzgkztfojzgkzcmmf4w65luknuxuzi): [removeLayoutComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3jpojsw233wmvggc6lpov2eg33nobxw4zlooq)
>
> :

## Method Types

---

> **All methods**
>
> : [EOForm](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3jpivhum33snu): [add](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3jpmfsgi)

## Constructors

---

### EOForm

`public EOForm( int rows, int columns, int rowSpacing, int columnSpacing)`

Description forthcoming.

---

## Instance Methods

---

### add

`public java.awt.Component add(java.awt.Component formCell)`

Adds _formCell_, an EOFormCell, to the receiver's collection of form cells.

---

### addLayoutComponent

`public void addLayoutComponent( String aString, java.awt.Component aComponent)`

Description forthcoming.

---

### layoutContainer

`public void layoutContainer(java.awt.Container formCell)`

Lays out the title and text field of _formCell_..

---

### minimumLayoutSize

`public java.awt.Dimension minimumLayoutSize(java.awt.Container aContainer)`

Returns the value returned from _aContainer_'s __getMinimumSize__..

---

### preferredLayoutSize

`public java.awt.Dimension preferredLayoutSize(java.awt.Container aContainer)`

Returns the value returned from _aContainer_'s __getPreferredSize__..

---

### removeLayoutComponent

`public void removeLayoutComponent(java.awt.Component aComponent)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOViewLayout.html
archived_at: '2026-07-15T08:13:54.830431Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOViewLayout

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : java.awt.LayoutManager2: java.io.Serializable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

EOViewLayout is an AWT LayoutManager for use in Java Client applications. It implements the geometry options available in Interface Builder's Size inspector. The size of a Component embedded in a Container using this layout will be a function of both its autosizing mask and its initial size (see [setAutosizingMask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5zwk5cbov2g643jpjuw4z2nmfzww) for details).

## Constants

---

EOViewLayout defines the following `int` constants:

- MaxXMargin
- MinXMargin
- MaxYMargin
- MinYMargin
- WidthSizable
- HeightSizable
- BothSizable

For more information on what these constants are and how they're used, see the method description for [setAutosizingMask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5zwk5cbov2g643jpjuw4z2nmfzww).

## Interfaces Implemented

---

> : java.awt.LayoutManager2
>
> : [addLayoutComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5qwizcmmf4w65luinxw24dpnzsw45a): [getLayoutAlignmentX](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5twk5cmmf4w65luifwgsz3onvsw45cy): [getLayoutAlignmentY](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5twk5cmmf4w65luifwgsz3onvsw45cz): [invalidateLayout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5uw45tbnruwiylumvggc6lpov2a): [maximumLayoutSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5wwc6djnv2w2tdbpfxxk5ctnf5gk)
>
> :
>
> : java.io.Serializable:

## Method Types

---

> **All methods**
>
> : [EOViewLayout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5cu6vtjmv3uyylzn52xi): [autosizingMask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5qxk5dponuxu2lom5gwc43l): [lastKnownSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5wgc43ujnxg653oknuxuzi): [layoutContainer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5wgc6lpov2eg33oorqws3tfoi): [minimumLayoutSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5wws3tjnv2w2tdbpfxxk5ctnf5gk): [preferredLayoutSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5yhezlgmvzhezlejrqxs33vorjws6tf): [removeLayoutComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5zgk3lpozsuyylzn52xiq3pnvyg63tfnz2a): [setAutosizingMask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5zwk5cbov2g643jpjuw4z2nmfzww): [setLastKnownSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5zwk5cmmfzxis3on53w4u3jpjsq)

## Constructors

---

### EOViewLayout

`public EOViewLayout()`

Description forthcoming.

---

## Instance Methods

---

### addLayoutComponent

`public void addLayoutComponent( String name, java.awt.Component aComponent)`

Description forthcoming.

---

### addLayoutComponent

`public void addLayoutComponent( java.awt.Component aComponent, Object constraints)`

Description forthcoming.

---

### autosizingMask

`public int autosizingMask(java.awt.Component aComponent)`

Description forthcoming.

---

### getLayoutAlignmentX

`public float getLayoutAlignmentX(java.awt.Container aContainer)`

Description forthcoming.

---

### getLayoutAlignmentY

`public float getLayoutAlignmentY(java.awt.Container aContainer)`

Description forthcoming.

---

### invalidateLayout

`public void invalidateLayout(java.awt.Container aContainer)`

Description forthcoming.

---

### lastKnownSize

`public java.awt.Dimension lastKnownSize(java.awt.Component aComponent)`

Description forthcoming.

---

### layoutContainer

`public void layoutContainer(java.awt.Container aContainer)`

Description forthcoming.

---

### maximumLayoutSize

`public java.awt.Dimension maximumLayoutSize(java.awt.Container aContainer)`

Description forthcoming.

---

### minimumLayoutSize

`public java.awt.Dimension minimumLayoutSize(java.awt.Container aContainer)`

Description forthcoming.

---

### preferredLayoutSize

`public java.awt.Dimension preferredLayoutSize(java.awt.Container aContainer)`

Description forthcoming.

---

### removeLayoutComponent

`public void removeLayoutComponent(java.awt.Component aComponent)`

Description forthcoming.

---

### setAutosizingMask

`public void setAutosizingMask( java.awt.Component aComponent, int mask)`

Sets the autosizing mask of _component_ to _mask_. This information is subsequently used by the receiver to calculate the new location and dimensions of _component_ whenever its parent is resized. The _mask_ should be some bitwise combination of the following:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| [MaxXMargin](#apple-ijdeurkcindeu) | the distance between _component_'s right edge and that of its parent may be adjusted |
| [MinXMargin](#apple-ijdeusseindus) | _component_'s left edge distance may be adjusted |
| [MaxYMargin](#apple-ijdeuscjizaug) | the distance between _component_'s bottom edge and that of its parent may be adjusted |
| [MinYMargin](#apple-ijdeursjizcec) | _component_'s top edge distance may be adjusted |
| [WidthSizable](#apple-ijdeussdi5buc) | _component_'s width may be adjusted |
| [HeightSizable](#apple-ijdeursii5cuu) | _component_'s height may be adjusted |
| [BothSizable](#apple-ijdeuskgivfeu) | both width and height may be adjusted |

Note that unless _mask_ is 0 (zero), the default mask, _component_'s adjusted size is a factor of its size when __setAutosizingMask__ was invoked.

---

### setLastKnownSize

`public void setLastKnownSize( java.awt.Component aComponent, java.awt.Dimension size)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

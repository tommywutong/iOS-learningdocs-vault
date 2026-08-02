---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOViewLayout.html
archived_at: '2026-07-15T08:11:45.160660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOViewLayout

> **__Inherits
> from:__**
> : Object

> **__Implements:__**
> : java.awt.LayoutManager2
> : java.awt.LayoutManager (java.awt.LayoutManager2)
> : java.io.Serializable

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOViewLayout is an AWT LayoutManager for use
in Java Client application (using com.apple.client.eointerface).
It implements the geometry options available in Interface Builder's
Size inspector. The size of a Component embedded in a Container
using this layout will be a function of both its autosizing mask
and its initial size (see [setAutosizingMask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5zwk5cbov2g643jpjuw4z2nmfzww) for
details).

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

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

For more information on what these constants are and how they're
used, see the method description for [setAutosizingMask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkzuwk52mmf4w65luf5zwk5cbov2g643jpjuw4z2nmfzww).

## Constructors

---

### `EOViewLayout`

`public EOViewLayout()`

Any consumers of EOViewLayout should use the [defaultInstance](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vtjmv3uyylzn52xil3emvtgc5lmorew443umfxggzi).

---

## Static Methods

---

### defaultInstance

`public static EOViewLayout defaultInstance()`

Returns that single instance of the receiver
used to lay out all InterfaceBuilder-generated Containers.

---

## Instance Methods

---

### setAutosizingMask

`public void setAutosizingMask(
java.awt.Component  component,
int  mask)`

Sets the autosizing mask of  _component_ to  _mask._
This information is subsequently used by the receiver to calculate
the new location and dimensions of  _component_ whenever
its parent is resized. The  _mask_ should be
some bitwise combination of the following:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| [MaxXMargin](#apple-ijdeurkcindeu) | the distance between  _component_'s right edge and that of its parent may be adjusted |
| [MinXMargin](#apple-ijdeusseindus) | _component_'s left edge distance may be adjusted |
| [MaxYMargin](#apple-ijdeuscjizaug) | the distance between  _component_'s bottom edge and that of its parent may be adjusted |
| [MinYMargin](#apple-ijdeursjizcec) | _component_'s top edge distance may be adjusted |
| [WidthSizable](#apple-ijdeussdi5buc) | _component_'s width may be adjusted |
| [HeightSizable](#apple-ijdeursii5cuu) | _component_'s height may be adjusted |
| [BothSizable](#apple-ijdeuskgivfeu) | both width and height may be adjusted |

Note that unless  _mask_ is
0 (zero), the default mask,  _component_'s
adjusted size is a factor of its size when `setAutosizingMask` was
invoked.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

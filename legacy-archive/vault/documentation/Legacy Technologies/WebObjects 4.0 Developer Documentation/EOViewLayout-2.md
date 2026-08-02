---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOViewLayout.html
archived_at: '2026-07-18T01:28:47.024923Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOTextAssociation-2.md)
[!](NSImage%20Additions.md)

---

# EOViewLayout

__Inherits From:__
Object

java.awt.LayoutManager2
java.io.Serializable

__Inherits From:__
com.apple.client.eointerface

---

## Class Description

EOViewLayout is an AWT LayoutManager that implements the geometry options available in InterfaceBuilder's Size inspector. The size of a Component embedded in a Container using this layout will be a function of both its autosizing mask and its initial size (see [`setAutosizingMask`](#apple-gm3tknq) for details).

EOViewLayout is for use in Java Client applications only; there isn't an equivalent class for Yellow Box.

---

## Constructors

public `EOViewLayout`()

Any consumers of EOViewLayout should use the [`defaultInstance`](#apple-gm3dcnq).

---

### defaultInstance

public static EOViewLayout `defaultInstance`()

Returns that single instance of the receiver used to lay out all InterfaceBuilder-generated Containers.

---

## Instance Methods

---

### setAutosizingMask

public void `setAutosizingMask`(java.awt.Component _component_, int _mask_)

Sets the autosizing mask of _component_ to _mask_. This information is subsequently used by the receiver to calculate the new location and dimensions of _component_ whenever its parent is resized. The _mask_ should be some bitwise combination of the following:

| Fixed | neither _component_'s location nor its dimensions may be adjusted |
| MaxXMargin | the distance between _component_'s right edge and that of its parent may be adjusted |
| MinXMargin | _component_'s left edge distance may be adjusted |
| MaxYMargin | the distance between _component_'s bottom edge and that of its parent may be adjusted |
| MinYMargin | _component_'s top edge distance may be adjusted |
| WidthSizable | _component_'s width may be adjusted |
| HeightSizable | _component_'s height may be adjusted |
| BothSizable | both width and height may be adjusted |

```
```

Note that unless _mask_ is Fixed (the default),_component_'s adjusted size will be some factor of its size at the moment `setAutosizingMask` was invoked.

---

[!](EOTextAssociation-2.md)
[!](NSImage%20Additions.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._

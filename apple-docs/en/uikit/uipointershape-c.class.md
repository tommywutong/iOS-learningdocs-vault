---
title: UIPointerShape
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointershape-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uipointershape-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointershape-c.class.json'
content_hash: 'sha256:4e6cd3a0435da6cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerShape

<sub>Class</sub>

An object that defines the shape of custom pointers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIPointerShape : NSObject
```

## Overview

If the desired pointer shape can be expressed as a rounded rectangle, use either [shapeWithRoundedRect:](uipointershape-c.class/shapewithroundedrect_.md) or [shapeWithRoundedRect:cornerRadius:](uipointershape-c.class/shapewithroundedrect_cornerradius_.md) for best results.

> [!note] Note
> If used alongside a content effect, this rectangle must be in the view coordinate space of the [preview](uipointereffect-swift.enum/preview.md). Otherwise, it’s centered about the pointer’s current location, and the rectangle’s origin is interpreted as an offset.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Specifying pointer shapes

- [beamWithPreferredLength:axis:](uipointershape-c.class/beamwithpreferredlength_axis_.md) — Morphs the pointer into a vertical or horizontal beam.
- [shapeWithPath:](uipointershape-c.class/shapewithpath_.md) — Morphs the pointer into the given Bézier path.
- [shapeWithRoundedRect:](uipointershape-c.class/shapewithroundedrect_.md) — Morphs the pointer into a rounded rectangle using the default corner radius.
- [shapeWithRoundedRect:cornerRadius:](uipointershape-c.class/shapewithroundedrect_cornerradius_.md) — Morphs the pointer into a rounded rectangle using the provided corner radius.

## See Also

### Pointer styles

- [UIPointerStyle](uipointerstyle.md) — An object that defines the pointer shape and effect.
- [UIPointerEffect](uipointereffect-c.class.md) — An effect that alters a view’s appearance when a pointer enters the current region.
- [UIPointerAccessory](uipointeraccessory.md) — Constants that describe accessories to display alongside the primary pointer.

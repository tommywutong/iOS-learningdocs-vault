---
title: bounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/bounds
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/bounds.json'
content_hash: 'sha256:431512312bfcfa7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# bounds

<sub>Instance Property</sub>

The bounding rectangle of the screen, measured in points.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

This rectangle is specified in the current coordinate space, which takes into account any interface rotations in effect for the device. Therefore, the value of this property may change when the device rotates between portrait and landscape orientations.

## See Also

### Getting the size and scale

- [nativeBounds](nativebounds.md) — The bounding rectangle of the physical screen, measured in pixels.
- [nativeScale](nativescale.md) — The native scale factor for the physical screen.
- [scale](scale.md) — The natural scale factor associated with the screen.

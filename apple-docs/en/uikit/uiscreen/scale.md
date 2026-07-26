---
title: scale
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/scale
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/scale.json'
content_hash: 'sha256:d26ef38b8029f0aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# scale

<sub>Instance Property</sub>

The natural scale factor associated with the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var scale: CGFloat { get }
```

## Discussion

This value reflects the scale factor needed to convert from the default logical coordinate space into the device coordinate space of this screen. The default logical coordinate space is measured using points. For Retina displays, the scale factor may be `3.0` or `2.0` and one point can represented by nine or four pixels, respectively. For standard-resolution displays, the scale factor is `1.0` and one point equals one pixel.

## See Also

### Getting the size and scale

- [bounds](bounds.md) — The bounding rectangle of the screen, measured in points.
- [nativeBounds](nativebounds.md) — The bounding rectangle of the physical screen, measured in pixels.
- [nativeScale](nativescale.md) — The native scale factor for the physical screen.

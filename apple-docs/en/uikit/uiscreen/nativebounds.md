---
title: nativeBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/nativebounds
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/nativebounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/nativebounds.json'
content_hash: 'sha256:29856333d38c5c47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# nativeBounds

<sub>Instance Property</sub>

The bounding rectangle of the physical screen, measured in pixels.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var nativeBounds: CGRect { get }
```

## Discussion

This rectangle is based on the device in a portrait-up orientation. This value does not change as the device rotates.

## See Also

### Getting the size and scale

- [bounds](bounds.md) — The bounding rectangle of the screen, measured in points.
- [nativeScale](nativescale.md) — The native scale factor for the physical screen.
- [scale](scale.md) — The natural scale factor associated with the screen.

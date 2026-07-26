---
title: shadowOffset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsshadow/shadowoffset
source_url: 'https://developer.apple.com/documentation/uikit/nsshadow/shadowoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsshadow/shadowoffset.json'
content_hash: 'sha256:1a4c3c6a86bc442e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSShadow](../nsshadow.md)

# shadowOffset

<sub>Instance Property</sub>

The shadow’s relative position, which you specify with horizontal and vertical offset values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var shadowOffset: CGSize { get set }
```

## Discussion

This property contains the horizontal and vertical offset values that you specify using the `width` and `height` fields of the `CGSize` or `NSSize` data type. These offsets use the default user coordinate space and are not affected by custom transformations. Positive offset values extend down and to the right from the user’s perspective.

> [!note] Note
> In macOS 10.15 and earlier, if you add a shadow to a layer that has a different graphics context, then positive offset values might extend up and to the right from the user’s perspective, instead of down and to the right as usual.

## See Also

### Managing a shadow

- [shadowBlurRadius](shadowblurradius.md) — The blur radius of the shadow.
- [shadowColor](shadowcolor.md) — The color of the shadow.

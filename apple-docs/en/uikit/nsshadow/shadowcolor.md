---
title: shadowColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsshadow/shadowcolor
source_url: 'https://developer.apple.com/documentation/uikit/nsshadow/shadowcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsshadow/shadowcolor.json'
content_hash: 'sha256:98d09921d90c26db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSShadow](../nsshadow.md)

# shadowColor

<sub>Instance Property</sub>

The color of the shadow.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var shadowColor: Any? { get set }
```

## Discussion

The default shadow color is black with an alpha of 1/3. If you set this property to `nil`, the shadow is not drawn. The color you specify must be convertible to an RGBA color and may contain alpha information.

## See Also

### Managing a shadow

- [shadowOffset](shadowoffset.md) — The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [shadowBlurRadius](shadowblurradius.md) — The blur radius of the shadow.

---
title: shadowBlurRadius
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsshadow/shadowblurradius
source_url: 'https://developer.apple.com/documentation/uikit/nsshadow/shadowblurradius'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsshadow/shadowblurradius.json'
content_hash: 'sha256:4207b6e17dafe828'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSShadow](../nsshadow.md)

# shadowBlurRadius

<sub>Instance Property</sub>

The blur radius of the shadow.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var shadowBlurRadius: CGFloat { get set }
```

## Discussion

This property contains the shadow’s blur radius, as measured in the default user coordinate space. A value of `0` produces no blur, while larger values produce an increasingly large blurred shadow. This value must not be negative. The default value is `0`.

## See Also

### Managing a shadow

- [shadowOffset](shadowoffset.md) — The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [shadowColor](shadowcolor.md) — The color of the shadow.

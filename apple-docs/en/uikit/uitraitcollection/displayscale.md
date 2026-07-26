---
title: displayScale
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/displayscale
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/displayscale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/displayscale.json'
content_hash: 'sha256:699d41f2d6b27358'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# displayScale

<sub>Instance Property</sub>

The display scale of the trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var displayScale: CGFloat { get }
```

## Discussion

A value of `1.0` indicates a non-Retina display, `2.0` indicates a Retina display, and `3.0` indicates a Super Retina display. The default display scale for a trait collection is `0.0` (indicating unspecified).

## See Also

### Retrieving display-related traits

- [displayGamut](displaygamut.md) — The gamut of the current display.
- [UIDisplayGamut](../uidisplaygamut.md) — Constants that indicate the gamut of the current display.

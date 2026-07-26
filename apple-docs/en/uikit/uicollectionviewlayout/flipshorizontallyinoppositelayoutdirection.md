---
title: flipsHorizontallyInOppositeLayoutDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/flipshorizontallyinoppositelayoutdirection
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/flipshorizontallyinoppositelayoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/flipshorizontallyinoppositelayoutdirection.json'
content_hash: 'sha256:f7c72bc5844d8ba1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# flipsHorizontallyInOppositeLayoutDirection

<sub>Instance Property</sub>

A Boolean value that indicates whether the horizontal coordinate system is automatically flipped at appropriate times.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var flipsHorizontallyInOppositeLayoutDirection: Bool { get }
```

## Discussion

The language you use during development naturally affects the decisions you make when configuring your layout object. When you develop using a left-to-right language, your layout information automatically matches the collection view’s natural coordinate system. However, when the user’s language has a right-to-left orientation, the layout information you provide is still based on the collection view’s natural coordinate system. This discrepancy can cause layout issues for languages using the opposite orientation. When this property is set to [true](../../swift/true.md), the collection view automatically flips the orientation of its horizontal coordinate system to match the leading edge of the current language. (The [developmentLayoutDirection](developmentlayoutdirection.md) property specifies the layout direction used to design the layout.) Flipping the horizontal coordinate system effectively flips your existing layout information, which should result in a better looking layout.

The default value of this property is [false](../../swift/false.md).

## See Also

### Supporting right-to-left layouts

- [developmentLayoutDirection](developmentlayoutdirection.md) — The direction of the language you used when designing your custom layout.

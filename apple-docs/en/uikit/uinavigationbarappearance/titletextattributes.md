---
title: titleTextAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbarappearance/titletextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbarappearance/titletextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbarappearance/titletextattributes.json'
content_hash: 'sha256:8ba6886fc7d61908'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarAppearance](../uinavigationbarappearance.md)

# titleTextAttributes

<sub>Instance Property</sub>

String attributes to apply to the text of a standard-size title.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var titleTextAttributes: [NSAttributedString.Key : Any] { get set }
```

## Discussion

If you don’t specify font or color attributes for the text, UIKit supplies appropriate default values. For a list of possible keys, see [NSAttributedString.Key](../../foundation/nsattributedstring/key.md).

## See Also

### Configuring the title

- [largeTitleTextAttributes](largetitletextattributes.md) — String attributes to apply to the text of a large-size title.
- [titlePositionAdjustment](titlepositionadjustment.md) — The distance, in points, by which to offset the title horizontally and vertically.

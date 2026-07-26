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
doc_path: /documentation/uikit/uibarbuttonitemstateappearance/titletextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemstateappearance/titletextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemstateappearance/titletextattributes.json'
content_hash: 'sha256:34d0439a21760a19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemStateAppearance](../uibarbuttonitemstateappearance.md)

# titleTextAttributes

<sub>Instance Property</sub>

String attributes to apply to the text of the bar button item’s title.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var titleTextAttributes: [NSAttributedString.Key : Any] { get set }
```

## Discussion

If you don’t specify font or color attributes for the text, UIKit supplies appropriate default values. For a list of possible keys, see [NSAttributedString.Key](../../foundation/nsattributedstring/key.md).

## See Also

### Configuring the title

- [titlePositionAdjustment](titlepositionadjustment.md) — The additional amount by which to offset the title horizontally and vertically.

---
title: compactScrollEdgeAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/compactscrolledgeappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/compactscrolledgeappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/compactscrolledgeappearance.json'
content_hash: 'sha256:0c0daaf59832543b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# compactScrollEdgeAppearance

<sub>Instance Property</sub>

The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var compactScrollEdgeAppearance: UINavigationBarAppearance? { get set }
```

## Discussion

When a compact-height navigation bar displays the top navigation item, the appearance setting in this property overrides the settings in the [compactScrollEdgeAppearance](../uinavigationbar/compactscrolledgeappearance.md) property of [UINavigationBar](../uinavigationbar.md).

Use this property to apply appearance settings to the navigation bar based on the navigation item stored in the [topItem](../uinavigationbar/topitem.md) property. If the top item’s [compactScrollEdgeAppearance](compactscrolledgeappearance.md) property is `nil`, UIKit uses the navigation bar’s compact scroll edge appearance.

## See Also

### Overriding the navigation bar’s appearance settings

- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [compactAppearance](compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

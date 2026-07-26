---
title: compactAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/compactappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/compactappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/compactappearance.json'
content_hash: 'sha256:11f7f7e1d36e62cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# compactAppearance

<sub>Instance Property</sub>

The appearance settings for a compact-height navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var compactAppearance: UINavigationBarAppearance? { get set }
```

## Discussion

When the navigation bar displays the current navigation item, the appearance settings in this property override the settings provided by the [compactAppearance](../uinavigationbar/compactappearance.md) property of [UINavigationBar](../uinavigationbar.md).

Use this property to apply appearance settings to the navigation bar based on the navigation item stored in the [topItem](../uinavigationbar/topitem.md) property. If the top item’s [compactAppearance](compactappearance.md) property is `nil`, UIKit uses the navigation bar’s compact appearance settings.

## See Also

### Overriding the navigation bar’s appearance settings

- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

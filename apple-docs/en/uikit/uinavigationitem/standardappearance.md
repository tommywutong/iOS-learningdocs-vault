---
title: standardAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/standardappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/standardappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/standardappearance.json'
content_hash: 'sha256:a63f750e7c71d6f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# standardAppearance

<sub>Instance Property</sub>

The appearance settings for a standard-height navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var standardAppearance: UINavigationBarAppearance? { get set }
```

## Discussion

When the navigation bar displays the current navigation item, the appearance settings in this property override the settings provided by the [standardAppearance](../uinavigationbar/standardappearance.md) property of [UINavigationBar](../uinavigationbar.md).

Use this property to apply appearance settings to the navigation bar based on the navigation item stored in the [topItem](../uinavigationbar/topitem.md) property. If the top item’s [standardAppearance](standardappearance.md) property is `nil`, UIKit uses the navigation bar’s appearance.

## See Also

### Overriding the navigation bar’s appearance settings

- [compactAppearance](compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

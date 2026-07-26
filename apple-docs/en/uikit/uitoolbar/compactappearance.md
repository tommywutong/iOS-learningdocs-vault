---
title: compactAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/compactappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/compactappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/compactappearance.json'
content_hash: 'sha256:5c04c3d9902e7eba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# compactAppearance

<sub>Instance Property</sub>

The appearance settings to use for a compact-height toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var compactAppearance: UIToolbarAppearance? { get set }
```

## Discussion

If the value of this property is `nil`, UIKit uses the same settings found in the [standardAppearance](standardappearance.md) property.

## See Also

### Customizing appearance

- [standardAppearance](standardappearance.md) — The appearance settings to use for a standard-height toolbar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](../uitoolbar-legacy-customizations.md) — Customize appearance information directly on the toolbar object.

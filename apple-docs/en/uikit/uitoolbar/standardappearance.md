---
title: standardAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/standardappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/standardappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/standardappearance.json'
content_hash: 'sha256:b90135a0381f6480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# standardAppearance

<sub>Instance Property</sub>

The appearance settings to use for a standard-height toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var standardAppearance: UIToolbarAppearance { get set }
```

## Discussion

The default value of this property is an appearance object containing the system’s default appearance settings.

## See Also

### Customizing appearance

- [compactAppearance](compactappearance.md) — The appearance settings to use for a compact-height toolbar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](../uitoolbar-legacy-customizations.md) — Customize appearance information directly on the toolbar object.

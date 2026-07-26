---
title: prominentButtonAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbarappearance/prominentbuttonappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbarappearance/prominentbuttonappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbarappearance/prominentbuttonappearance.json'
content_hash: 'sha256:f46f64e4f0c86159'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbarAppearance](../uitoolbarappearance.md)

# prominentButtonAppearance

<sub>Instance Property</sub>

The appearance attributes for Prominent buttons.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var prominentButtonAppearance: UIBarButtonItemAppearance { get set }
```

## Discussion

Use this property to configure the appearance of bar button items that use `UIBarButtonItemStyleProminent`. If the navigation bar doesn’t have any buttons using this style, this property has no effect.

## See Also

### Configuring bar button items

- [buttonAppearance](buttonappearance.md) — The appearance attributes for plain bar button items in the toolbar.

---
title: prominentButtonAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbarappearance/prominentbuttonappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbarappearance/prominentbuttonappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbarappearance/prominentbuttonappearance.json'
content_hash: 'sha256:230389051aefafb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarAppearance](../uinavigationbarappearance.md)

# prominentButtonAppearance

<sub>Instance Property</sub>

The appearance attributes for Prominent buttons.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var prominentButtonAppearance: UIBarButtonItemAppearance { get set }
```

## Discussion

Use this property to configure the appearance of bar button items that use `UIBarButtonItemStyleProminent`. If the navigation bar doesn’t have any buttons using this style, this property has no effect.

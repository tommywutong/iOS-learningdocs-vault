---
title: doneButtonAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（26.0 起废弃）, iPadOS 13.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 13.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uinavigationbarappearance/donebuttonappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbarappearance/donebuttonappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbarappearance/donebuttonappearance.json'
content_hash: 'sha256:ca86348cc2b74dbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarAppearance](../uinavigationbarappearance.md)

# doneButtonAppearance

<sub>Instance Property</sub>

The appearance attributes for Done buttons.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var doneButtonAppearance: UIBarButtonItemAppearance { get set }
```

## Discussion

Use this property to configure the appearance of bar button items that use the [UIBarButtonItemStyleDone](../uibarbuttonitem/style-swift.enum/done.md) style, when appropriate. If the navigation bar doesn’t have a done button, setting the value of this property has no effect.

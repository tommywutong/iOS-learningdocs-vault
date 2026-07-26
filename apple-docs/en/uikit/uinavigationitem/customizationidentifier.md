---
title: customizationIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/customizationidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/customizationidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/customizationidentifier.json'
content_hash: 'sha256:a2f9ad20287bbf4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# customizationIdentifier

<sub>Instance Property</sub>

A globally unique string that enables user customization of the navigation bar layout.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var customizationIdentifier: String? { get set }
```

## Discussion

Set a customization identifier to support a personalized navigation bar layout experience. When you assign a string to this property, UIKit allows people to customize the layout of the items in the navigation bar by choosing the customize option in the overflow menu. UIKit automatically saves and restores this custom layout across app launches.

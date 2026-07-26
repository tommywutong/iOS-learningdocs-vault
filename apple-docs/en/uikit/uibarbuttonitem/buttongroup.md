---
title: buttonGroup
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/buttongroup
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/buttongroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/buttongroup.json'
content_hash: 'sha256:6e955ef4a4ad7c89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# buttonGroup

<sub>Instance Property</sub>

The group that the button belongs to.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var buttonGroup: UIBarButtonItemGroup? { get }
```

## Discussion

This property contains the group to which the item belongs. This property is configured automatically when you add the bar button item to a [UIBarButtonItemGroup](../uibarbuttonitemgroup.md) object. If the item isn’t associated with a bar button item group, this property is `nil`.

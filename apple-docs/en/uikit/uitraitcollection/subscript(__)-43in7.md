---
title: 'subscript(_:)'
framework: UIKit
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/subscript(_:)-43in7'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/subscript(_:)-43in7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/subscript%28_%3A%29-43in7.json'
content_hash: 'sha256:172492ce8c066f01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
subscript<T>(trait: T.Type) -> T.Value where T : UITraitDefinition { get }
```

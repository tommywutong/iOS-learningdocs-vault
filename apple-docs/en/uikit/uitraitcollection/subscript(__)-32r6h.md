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
doc_path: '/documentation/uikit/uitraitcollection/subscript(_:)-32r6h'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/subscript(_:)-32r6h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/subscript%28_%3A%29-32r6h.json'
content_hash: 'sha256:1e1979fffeb824c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
subscript<T>(trait: T.Type) -> T.Value where T : UITraitDefinition, T.Value == Int { get }
```

---
title: 'replacing(_:value:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/replacing(_:value:)-o6qa'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/replacing(_:value:)-o6qa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/replacing%28_%3Avalue%3A%29-o6qa.json'
content_hash: 'sha256:68c41c81960fab8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# replacing(_:value:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replacing<T>(_ trait: T.Type, value: T.Value) -> UITraitCollection where T : UITraitDefinition, T.Value == CGFloat?
```

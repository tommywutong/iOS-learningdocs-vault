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
doc_path: '/documentation/uikit/uitraitcollection/replacing(_:value:)-4c3s8'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/replacing(_:value:)-4c3s8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/replacing%28_%3Avalue%3A%29-4c3s8.json'
content_hash: 'sha256:9d0e2f8b7b6692dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# replacing(_:value:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replacing<T>(_ trait: T.Type, value: T.Value) -> UITraitCollection where T : _UICustomRawRepresentableTraitDefinition, T._CustomRawValue == Double
```

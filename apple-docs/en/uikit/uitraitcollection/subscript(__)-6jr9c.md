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
doc_path: '/documentation/uikit/uitraitcollection/subscript(_:)-6jr9c'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/subscript(_:)-6jr9c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/subscript%28_%3A%29-6jr9c.json'
content_hash: 'sha256:2e2f034f4ba78bf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
subscript<T>(trait: T.Type) -> T.Value where T : _UICustomRawRepresentableTraitDefinition, T._CustomRawValue == Int { get }
```

---
title: 'init(_:value:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/init(_:value:)-59di1'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/init(_:value:)-59di1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/init%28_%3Avalue%3A%29-59di1.json'
content_hash: 'sha256:debe1d5b60a2603d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# init(_:value:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init<T>(_ trait: T.Type, value: T.Value) where T : _UICustomRawRepresentableTraitDefinition, T._CustomRawValue == Double
```

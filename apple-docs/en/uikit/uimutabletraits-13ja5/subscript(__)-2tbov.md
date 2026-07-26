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
doc_path: '/documentation/uikit/uimutabletraits-13ja5/subscript(_:)-2tbov'
source_url: 'https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5/subscript(_:)-2tbov'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutabletraits-13ja5/subscript%28_%3A%29-2tbov.json'
content_hash: 'sha256:5c85537c1d701af6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableTraits](../uimutabletraits-13ja5.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
subscript<T>(trait: T.Type) -> T.Value where T : UITraitDefinition, T.Value == CGFloat? { get set }
```

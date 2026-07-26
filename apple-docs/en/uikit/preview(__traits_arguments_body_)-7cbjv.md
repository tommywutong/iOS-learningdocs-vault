---
title: 'Preview(_:traits:arguments:body:)'
framework: UIKit
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/preview(_:traits:arguments:body:)-7cbjv'
source_url: 'https://developer.apple.com/documentation/uikit/preview(_:traits:arguments:body:)-7cbjv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/preview%28_%3Atraits%3Aarguments%3Abody%3A%29-7cbjv.json'
content_hash: 'sha256:420fef08f5c3bb9d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Preview(_:traits:arguments:body:)

<sub>Macro</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@freestanding(declaration) macro Preview<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @PreviewBodyBuilder<UIViewController> body: @escaping @MainActor (T) -> UIViewController)
```

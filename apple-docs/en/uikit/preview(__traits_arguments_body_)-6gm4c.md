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
doc_path: '/documentation/uikit/preview(_:traits:arguments:body:)-6gm4c'
source_url: 'https://developer.apple.com/documentation/uikit/preview(_:traits:arguments:body:)-6gm4c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/preview%28_%3Atraits%3Aarguments%3Abody%3A%29-6gm4c.json'
content_hash: 'sha256:40e7e4781760d524'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Preview(_:traits:arguments:body:)

<sub>Macro</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@freestanding(declaration) macro Preview<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @PreviewBodyBuilder<UIView> body: @escaping @MainActor (T) -> UIView)
```

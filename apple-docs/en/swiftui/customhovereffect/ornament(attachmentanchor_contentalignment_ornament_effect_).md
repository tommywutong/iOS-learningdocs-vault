---
title: 'ornament(attachmentAnchor:contentAlignment:ornament:effect:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:effect:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:effect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/ornament%28attachmentanchor%3Acontentalignment%3Aornament%3Aeffect%3A%29.json'
content_hash: 'sha256:45ae42b32faf6ec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# ornament(attachmentAnchor:contentAlignment:ornament:effect:)

<sub>Type Method</sub>

Presents an ornament on hover.

<sub>visionOS</sub>

```swift
nonisolated static func ornament<Content, EffectContent>(attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D = .center, @ContentBuilder ornament: () -> Content, effect: @escaping (EmptyHoverEffectContent, Bool, GeometryProxy) -> EffectContent) -> OrnamentHoverContentEffect<Content, EffectContent> where Self == OrnamentHoverContentEffect<Content, EffectContent>, Content : View, EffectContent : HoverEffectContent
```

## Parameters

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the ornament.

- `contentAlignment` — The alignment of the ornament with its attachment anchor.

- `ornament` — The content of the ornament.

- `effect` — The effect used to present the ornament.

## Discussion

Use this method to present an ornament at the specified position when the view is hovered. The ornament will be presented using the provided `effect`.

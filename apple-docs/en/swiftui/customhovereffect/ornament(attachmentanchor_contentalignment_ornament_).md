---
title: 'ornament(attachmentAnchor:contentAlignment:ornament:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/ornament%28attachmentanchor%3Acontentalignment%3Aornament%3A%29.json'
content_hash: 'sha256:f64db86fb4cd7293'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# ornament(attachmentAnchor:contentAlignment:ornament:)

<sub>Type Method</sub>

Presents an ornament on hover.

<sub>visionOS</sub>

```swift
nonisolated static func ornament<Content>(attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D = .center, @ContentBuilder ornament: () -> Content) -> OrnamentHoverEffect<Content> where Self == OrnamentHoverEffect<Content>, Content : View
```

## Parameters

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the ornament.

- `contentAlignment` — The alignment of the ornament with its attachment anchor.

- `ornament` — The content of the ornament.

## Discussion

Use this method to show an ornament at the specified position when the view is hovered. The ornament will be shown with the default fade animation.

---
title: 'ornament(visibility:attachmentAnchor:contentAlignment:ornament:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ornament%28visibility%3Aattachmentanchor%3Acontentalignment%3Aornament%3A%29.json'
content_hash: 'sha256:b5948924b56195c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# ornament(visibility:attachmentAnchor:contentAlignment:ornament:)

<sub>Instance Method</sub>

Presents an ornament.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func ornament<Content>(visibility: Visibility = .automatic, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D = .back, @ContentBuilder ornament: () -> Content) -> some View where Content : View

```

## Parameters

- `visibility` — The visibility of the ornament.

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the ornament.

- `contentAlignment` — The alignment of the ornament with its attachment anchor.

## Discussion

Use this method to show an ornament at the specified position. The example below displays an ornament below the window:

```swift
Text("A view with an ornament")
    .ornament(attachmentAnchor: .scene(.bottom)) {
        OrnamentContent()
    }
```

## See Also

### Creating an ornament

- [OrnamentAttachmentAnchor](../ornamentattachmentanchor.md) — An attachment anchor for an ornament.

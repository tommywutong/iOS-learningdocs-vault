---
title: 'mask(alignment:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/mask(alignment:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/mask(alignment:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/mask%28alignment%3A_%3A%29.json'
content_hash: 'sha256:99995986fc8b8096'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# mask(alignment:_:)

<sub>Instance Method</sub>

Masks this view using the alpha channel of the given view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func mask<Mask>(alignment: Alignment = .center, @ContentBuilder _ mask: () -> Mask) -> some View where Mask : View

```

## Parameters

- `alignment` — The alignment for `mask` in relation to this view.

- `mask` — The view whose alpha the rendering system applies to the specified view.

## Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

```swift
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask {
        Rectangle().opacity(0.1)
    }
```

![A screenshot of a view masked by a rectangle with 10%](../../../../attachments/eb80d49199cb4ce05352313feb4e29e5/SwiftUI-View-mask@2x.png)

## See Also

### Masking and clipping

- [clipped(antialiased:)](<clipped(antialiased_).md>) — Clips this view to its bounding rectangular frame.
- [clipShape(_:style:)](<clipshape(__style_).md>) — Sets a clipping shape for this view.

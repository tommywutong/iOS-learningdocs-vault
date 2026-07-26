---
title: 'clipped(antialiased:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/clipped(antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/clipped(antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/clipped%28antialiased%3A%29.json'
content_hash: 'sha256:70ed95196cd32f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# clipped(antialiased:)

<sub>Instance Method</sub>

Clips this view to its bounding rectangular frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func clipped(antialiased: Bool = false) -> some View

```

## Parameters

- `antialiased` — A Boolean value that indicates whether the rendering system applies smoothing to the edges of the clipping rectangle.

## Return Value

A view that clips this view to its bounding frame.

## Discussion

Use the `clipped(antialiased:)` modifier to hide any content that extends beyond the layout bounds of the shape.

By default, a view’s bounding frame is used only for layout, so any content that extends beyond the edges of the frame is still visible.

```swift
Text("This long text string is clipped")
    .fixedSize()
    .frame(width: 175, height: 100)
    .clipped()
    .border(Color.gray)
```

![Screenshot showing text clipped to its](../../../../attachments/e4c793f7bce8e09c9377a929b96e73e7/SwiftUI-View-clipped@2x.png)

## See Also

### Masking and clipping

- [mask(alignment:_:)](<mask(alignment___).md>) — Masks this view using the alpha channel of the given view.
- [clipShape(_:style:)](<clipshape(__style_).md>) — Sets a clipping shape for this view.

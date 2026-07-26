---
title: 'resizable(capInsets:resizingMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/resizable(capinsets:resizingmode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/resizable(capinsets:resizingmode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/resizable%28capinsets%3Aresizingmode%3A%29.json'
content_hash: 'sha256:0f12079ba73b1845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# resizable(capInsets:resizingMode:)

<sub>Instance Method</sub>

Sets the mode by which SwiftUI resizes an image to fit its space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resizable(capInsets: EdgeInsets = EdgeInsets(), resizingMode: Image.ResizingMode = .stretch) -> Image
```

## Parameters

- `capInsets` — Inset values that indicate a portion of the image that SwiftUI doesn’t resize.

- `resizingMode` — The mode by which SwiftUI resizes the image.

## Return Value

An image, with the new resizing behavior set.

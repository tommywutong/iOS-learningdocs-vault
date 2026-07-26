---
title: 'init(image:sourceRect:scale:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/imagepaint/init(image:sourcerect:scale:)'
source_url: 'https://developer.apple.com/documentation/swiftui/imagepaint/init(image:sourcerect:scale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagepaint/init%28image%3Asourcerect%3Ascale%3A%29.json'
content_hash: 'sha256:c882c737de549c48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImagePaint](../imagepaint.md)

# init(image:sourceRect:scale:)

<sub>Initializer</sub>

Creates a shape-filling shape style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(image: Image, sourceRect: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1), scale: CGFloat = 1)
```

## Parameters

- `image` — The image to be drawn.

- `sourceRect` — A unit-space rectangle defining how much of the source image to draw. The results are undefined if `sourceRect` selects areas outside the `[0, 1]` range in either axis.

- `scale` — A scale factor applied to the image during rendering.

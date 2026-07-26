---
title: 'init(size:format:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsimagerenderer/init(size:format:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/init(size:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderer/init%28size%3Aformat%3A%29.json'
content_hash: 'sha256:cb30e6a614d2c673'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md)

# init(size:format:)

<sub>Initializer</sub>

Creates an image renderer with the specified size and format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(size: CGSize, format: UIGraphicsImageRendererFormat)
```

## Parameters

- `size` — The size of images output from the renderer, specified in points.

- `format` — A [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md) object that encapsulates the format used to create the renderer context.

## Return Value

An initialized renderer.

## Discussion

Use this initializer to create an image renderer when you want to override the default format for the current device. Provide the size of the images you want to create, and an instance of [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md) with the required configuration.

## See Also

### Initializing an image renderer

- [- initWithBounds:format:](<init(bounds_format_).md>) — Creates an image renderer with the specified bounds and format.
- [- initWithSize:](<init(size_).md>) — Creates an image renderer for drawing images of the specified size.

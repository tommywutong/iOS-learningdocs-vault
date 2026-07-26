---
title: 'init(bounds:format:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsimagerenderer/init(bounds:format:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/init(bounds:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderer/init%28bounds%3Aformat%3A%29.json'
content_hash: 'sha256:fa7da7a4338f8bcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md)

# init(bounds:format:)

<sub>Initializer</sub>

Creates an image renderer with the specified bounds and format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(bounds: CGRect, format: UIGraphicsImageRendererFormat)
```

## Parameters

- `bounds` — The bounds of the image context the image renderer creates and subsequently draws upon. Specify values in points in the Core Graphics coordinate space.

- `format` — A [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md) object that encapsulates the format used to create the renderer context.

## Return Value

An initialized image renderer.

## Discussion

Use this initializer to create an image renderer when you want to override the default format for the current device.

## See Also

### Initializing an image renderer

- [- initWithSize:](<init(size_).md>) — Creates an image renderer for drawing images of the specified size.
- [- initWithSize:format:](<init(size_format_).md>) — Creates an image renderer with the specified size and format.

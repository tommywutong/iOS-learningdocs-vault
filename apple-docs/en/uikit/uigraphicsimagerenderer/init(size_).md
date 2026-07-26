---
title: 'init(size:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsimagerenderer/init(size:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/init(size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderer/init%28size%3A%29.json'
content_hash: 'sha256:71e960e2a9b17606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md)

# init(size:)

<sub>Initializer</sub>

Creates an image renderer for drawing images of the specified size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(size: CGSize)
```

## Parameters

- `size` — The size of images output from the renderer, specified in points.

## Return Value

An initialized image renderer.

## Discussion

Use this initializer to create an image renderer that will draw images of a given size. This renderer uses the [+ defaultFormat](<../uigraphicsrendererformat/default().md>) static method on [UIGraphicsImageRendererContext](../uigraphicsimagerenderercontext.md) to create its context, thereby selecting parameters that are the most appropriate for the current device.

## See Also

### Initializing an image renderer

- [- initWithBounds:format:](<init(bounds_format_).md>) — Creates an image renderer with the specified bounds and format.
- [- initWithSize:format:](<init(size_format_).md>) — Creates an image renderer with the specified size and format.

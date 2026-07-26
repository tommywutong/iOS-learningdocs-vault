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
doc_path: '/documentation/uikit/uigraphicsrenderer/init(bounds:format:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer/init(bounds:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer/init%28bounds%3Aformat%3A%29.json'
content_hash: 'sha256:3e6ff1de69fe5bec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRenderer](../uigraphicsrenderer.md)

# init(bounds:format:)

<sub>Initializer</sub>

Creates a new graphics renderer with the given bounds and format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(bounds: CGRect, format: UIGraphicsRendererFormat)
```

## Parameters

- `bounds` — The bounds of the Core Graphics context available to the renderer, with values measured in points.

- `format` — The format applied to the renderer’s context. This object is an instance of the subclass of [UIGraphicsRendererFormat](../uigraphicsrendererformat.md) appropriate for the concrete subclass of `UIGraphicsRenderer` you are using.

## Return Value

An initialized graphics renderer.

## Discussion

Use this initializer to create a graphics renderer when you want to override the default format for the current device.

The format instance is copied at initialization time, so you can immediately reuse the same instance to create additional renderers.

## See Also

### Initializing a graphics renderer

- [- initWithBounds:](<init(bounds_).md>) — Creates a new graphics renderer with the specified bounds and a default format.

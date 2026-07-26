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
doc_path: '/documentation/uikit/uigraphicspdfrenderer/init(bounds:format:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/init(bounds:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderer/init%28bounds%3Aformat%3A%29.json'
content_hash: 'sha256:5b69638a15c12d87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md)

# init(bounds:format:)

<sub>Initializer</sub>

Creates a new graphics renderer with the specified bounds and format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(bounds: CGRect, format: UIGraphicsPDFRendererFormat)
```

## Parameters

- `bounds` — The bounds of the Core Graphics context available to the renderer, with values in points.

- `format` — A [UIGraphicsPDFRendererFormat](../uigraphicspdfrendererformat.md) object that encapsulates the format applied to the renderer’s context.

## Return Value

An initialized PDF graphics renderer.

## Discussion

Use this initializer to create a PDF renderer when you want to override the default format for the current device. Otherwise, use the [- initWithBounds:](<../uigraphicsrenderer/init(bounds_).md>) method present on the abstract superclass, [UIGraphicsRenderer](../uigraphicsrenderer.md).

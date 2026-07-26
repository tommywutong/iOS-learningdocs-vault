---
title: 'init(bounds:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsrenderer/init(bounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer/init(bounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer/init%28bounds%3A%29.json'
content_hash: 'sha256:d2cb0397ba722cdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRenderer](../uigraphicsrenderer.md)

# init(bounds:)

<sub>Initializer</sub>

Creates a new graphics renderer with the specified bounds and a default format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(bounds: CGRect)
```

## Parameters

- `bounds` — The bounds of the Core Graphics context available to the renderer, with values measured in points.

## Return Value

An initialized graphics renderer.

## Discussion

Use this initializer to create a graphics renderer that operates on Core Graphics contexts with the specified bounds. This initializer uses the [+ defaultFormat](<../uigraphicsrendererformat/default().md>) static method on [UIGraphicsRendererFormat](../uigraphicsrendererformat.md) to create the renderer’s format, thereby selecting parameters that are the most appropriate for the current device.

## See Also

### Initializing a graphics renderer

- [- initWithBounds:format:](<init(bounds_format_).md>) — Creates a new graphics renderer with the given bounds and format.

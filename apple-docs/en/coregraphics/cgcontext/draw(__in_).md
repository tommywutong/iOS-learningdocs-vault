---
title: 'draw(_:in:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/draw(_:in:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/draw(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/draw%28_%3Ain%3A%29.json'
content_hash: 'sha256:fb1c79381e85b527'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# draw(_:in:)

<sub>Instance Method</sub>

Draws the contents of a layer object into the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(_ layer: CGLayer, in rect: CGRect)
```

## Parameters

- `layer` — The layer whose contents you want to draw.

- `rect` — The rectangle, in current user space coordinates, to draw in.

## Discussion

The contents are scaled, if necessary, to fit into the rectangle.

## See Also

### Drawing Core Graphics Layers

- [draw(_:at:)](<draw(__at_).md>) — Draws the contents of a layer object at the specified point.

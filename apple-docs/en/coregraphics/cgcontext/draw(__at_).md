---
title: 'draw(_:at:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/draw(_:at:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/draw(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/draw%28_%3Aat%3A%29.json'
content_hash: 'sha256:9f84199d1910f380'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# draw(_:at:)

<sub>Instance Method</sub>

Draws the contents of a layer object at the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(_ layer: CGLayer, at point: CGPoint)
```

## Parameters

- `layer` — The layer whose contents you want to draw.

- `point` — The location, in current user space coordinates, to use as the origin for the drawing.

## Discussion

Calling this method is equivalent to calling the [draw(_:in:)](<draw(__in_).md>) method with a rectangle whose origin is the specified point and whose size matches that of the specified layer.

## See Also

### Drawing Core Graphics Layers

- [draw(_:in:)](<draw(__in_).md>) — Draws the contents of a layer object into the specified rectangle.

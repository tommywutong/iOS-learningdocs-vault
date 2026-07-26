---
title: 'scaleBy(x:y:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/scaleby(x:y:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/scaleby(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/scaleby%28x%3Ay%3A%29.json'
content_hash: 'sha256:a4cf0fed3d4ce570'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# scaleBy(x:y:)

<sub>Instance Method</sub>

Changes the scale of the user coordinate system in a context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scaleBy(x sx: CGFloat, y sy: CGFloat)
```

## Parameters

- `sx` — The factor by which to scale the x-axis of the coordinate space of the specified context.

- `sy` — The factor by which to scale the y-axis of the coordinate space of the specified context.

## See Also

### Working with the Current Transformation Matrix

- [CGContextGetCTM](ctm.md) — Returns the current transformation matrix.
- [CGContextRotateCTM](<rotate(by_).md>) — Rotates the user coordinate system in a context.
- [CGContextTranslateCTM](<translateby(x_y_).md>) — Changes the origin of the user coordinate system in a context.
- [CGContextConcatCTM](<concatenate(__).md>) — Transforms the user coordinate system in a context using a specified matrix.

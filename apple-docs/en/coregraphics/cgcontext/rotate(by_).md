---
title: 'rotate(by:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/rotate(by:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/rotate(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/rotate%28by%3A%29.json'
content_hash: 'sha256:128fc09e4daf8082'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# rotate(by:)

<sub>Instance Method</sub>

Rotates the user coordinate system in a context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rotate(by angle: CGFloat)
```

## Parameters

- `angle` — The angle, in radians, by which to rotate the coordinate space of the specified context. Positive values rotate counterclockwise and negative values rotate clockwise.)

## Discussion

The direction that the context is rotated may appear to be altered by the state of the current transformation matrix prior to executing this function. For example, on iOS, a [UIView](../../uikit/uiview.md) applies a transformation to the graphics context that inverts the Y-axis (by multiplying it by `-1`). Rotating the user coordinate system on coordinate system that was previously flipped results in a rotation in the opposite direction (that is, positive values appear to rotate the coordinate system in the clockwise direction).

## See Also

### Working with the Current Transformation Matrix

- [CGContextGetCTM](ctm.md) — Returns the current transformation matrix.
- [CGContextScaleCTM](<scaleby(x_y_).md>) — Changes the scale of the user coordinate system in a context.
- [CGContextTranslateCTM](<translateby(x_y_).md>) — Changes the origin of the user coordinate system in a context.
- [CGContextConcatCTM](<concatenate(__).md>) — Transforms the user coordinate system in a context using a specified matrix.

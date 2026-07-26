---
title: 'CGAffineTransformMakeScale(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransformmakescale(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransformmakescale(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransformmakescale%28_%3A_%3A%29.json'
content_hash: 'sha256:9312b5894e421320'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformMakeScale(_:_:)

<sub>Function</sub>

Returns an affine transformation matrix constructed from scaling values you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformMakeScale(_ sx: CGFloat, _ sy: CGFloat) -> CGAffineTransform
```

## Parameters

- `sx` — The factor by which to scale the x-axis of the coordinate system.

- `sy` — The factor by which to scale the y-axis of the coordinate system.

## Return Value

A new affine transformation matrix.

## Discussion

This function creates a `CGAffineTransform` structure, which you can use (and reuse, if you want) to scale a coordinate system. The matrix takes the following form:

![A 3 by 3 matrix used to scale.](../../../attachments/9f887f1de9bbcb61af9992432fb821eb/media-1966736@2x.png)

Because the third column is always `(0,0,1)`, the `CGAffineTransform` data structure returned by this function contains values for only the first two columns.

These are the resulting equations used to scale the coordinates of a point (x,y):

![Scaling equations.](../../../attachments/31382764681648947a31bcd32a01d6e5/media-1966741@2x.png)

If you want only to scale an object to be drawn, it is not necessary to construct an affine transform to do so. The most direct way to scale your drawing is by calling the function [CGContextScaleCTM](<cgcontext/scaleby(x_y_).md>).

## See Also

### Creating an Affine Transformation Matrix

- [CGAffineTransformMake](<cgaffinetransformmake(____________).md>) — Returns an affine transformation matrix constructed from values you provide.
- [CGAffineTransformMakeRotation](<cgaffinetransformmakerotation(__).md>) — Returns an affine transformation matrix constructed from a rotation value you provide.
- [CGAffineTransformMakeTranslation](<cgaffinetransformmaketranslation(____).md>) — Returns an affine transformation matrix constructed from translation values you provide.

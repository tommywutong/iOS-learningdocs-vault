---
title: 'CGAffineTransformMakeRotation(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransformmakerotation(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransformmakerotation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransformmakerotation%28_%3A%29.json'
content_hash: 'sha256:3e45d989b37b3561'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformMakeRotation(_:)

<sub>Function</sub>

Returns an affine transformation matrix constructed from a rotation value you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformMakeRotation(_ angle: CGFloat) -> CGAffineTransform
```

## Parameters

- `angle` — The angle, in radians, by which this matrix rotates the coordinate system axes. In iOS, a positive value specifies counterclockwise rotation and a negative value specifies clockwise rotation. In macOS, a positive value specifies clockwise rotation and a negative value specifies counterclockwise rotation.

## Return Value

A new affine transformation matrix.

## Discussion

This function creates a `CGAffineTransform` structure, which you can use (and reuse, if you want) to rotate a coordinate system. The matrix takes the following form:

![A 3 by 3 matrix.](../../../attachments/208a3d614f01846a4816496780b1a1fb/media-1966725@2x.png)

The actual direction of rotation is dependent on the coordinate system orientation of the target platform, which is different in iOS and macOS. Because the third column is always `(0,0,1)`, the `CGAffineTransform` data structure returned by this function contains values for only the first two columns.

These are the resulting equations used to apply the rotation to a point (x, y):

![Rotation equations.](../../../attachments/6aee9efda1c1ac989f5c0fceb3b21a44/media-1966730@2x.png)

If you want only to rotate an object to be drawn, it is not necessary to construct an affine transform to do so. The most direct way to rotate your drawing is by calling the function [CGContextRotateCTM](<cgcontext/rotate(by_).md>).

## See Also

### Creating an Affine Transformation Matrix

- [CGAffineTransformMake](<cgaffinetransformmake(____________).md>) — Returns an affine transformation matrix constructed from values you provide.
- [CGAffineTransformMakeScale](<cgaffinetransformmakescale(____).md>) — Returns an affine transformation matrix constructed from scaling values you provide.
- [CGAffineTransformMakeTranslation](<cgaffinetransformmaketranslation(____).md>) — Returns an affine transformation matrix constructed from translation values you provide.

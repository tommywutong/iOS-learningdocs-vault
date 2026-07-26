---
title: 'CGAffineTransformRotate(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransformrotate(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransformrotate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransformrotate%28_%3A_%3A%29.json'
content_hash: 'sha256:3901ca710fe02965'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformRotate(_:_:)

<sub>Function</sub>

Returns an affine transformation matrix constructed by rotating an existing affine transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformRotate(_ t: CGAffineTransform, _ angle: CGFloat) -> CGAffineTransform
```

## Parameters

- `t` — An existing affine transform.

- `angle` — The angle, in radians, by which to rotate the affine transform. In iOS, a positive value specifies counterclockwise rotation and a negative value specifies clockwise rotation. In macOS, a positive value specifies clockwise rotation and a negative value specifies counterclockwise rotation.

## Return Value

A new affine transformation matrix.

## Discussion

You use this function to create a new affine transformation matrix by adding a rotation value to an existing affine transform. The resulting structure represents a new affine transform, which you can use (and reuse, if you want) to rotate a coordinate system.

The actual direction of rotation is dependent on the coordinate system orientation of the target platform, which is different in iOS and macOS.

## See Also

### Modifying Affine Transformations

- [CGAffineTransformTranslate](<cgaffinetransformtranslate(______).md>) — Returns an affine transformation matrix constructed by translating an existing affine transform.
- [CGAffineTransformScale](<cgaffinetransformscale(______).md>) — Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [CGAffineTransformInvert](<cgaffinetransforminvert(__).md>) — Returns an affine transformation matrix constructed by inverting an existing affine transform.
- [CGAffineTransformConcat](<cgaffinetransformconcat(____).md>) — Returns an affine transformation matrix constructed by combining two existing affine transforms.

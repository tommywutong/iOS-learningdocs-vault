---
title: 'CGAffineTransformTranslate(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransformtranslate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransformtranslate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransformtranslate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e2e6f52d932b767d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformTranslate(_:_:_:)

<sub>Function</sub>

Returns an affine transformation matrix constructed by translating an existing affine transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformTranslate(_ t: CGAffineTransform, _ tx: CGFloat, _ ty: CGFloat) -> CGAffineTransform
```

## Parameters

- `t` — An existing affine transform.

- `tx` — The value by which to move x values with the affine transform.

- `ty` — The value by which to move y values with the affine transform.

## Return Value

A new affine transformation matrix.

## Discussion

You use this function to create a new affine transform by adding translation values to an existing affine transform. The resulting structure represents a new affine transform, which you can use (and reuse, if you want) to move a coordinate system.

## See Also

### Modifying Affine Transformations

- [CGAffineTransformScale](<cgaffinetransformscale(______).md>) — Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [CGAffineTransformRotate](<cgaffinetransformrotate(____).md>) — Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [CGAffineTransformInvert](<cgaffinetransforminvert(__).md>) — Returns an affine transformation matrix constructed by inverting an existing affine transform.
- [CGAffineTransformConcat](<cgaffinetransformconcat(____).md>) — Returns an affine transformation matrix constructed by combining two existing affine transforms.

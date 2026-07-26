---
title: 'CGAffineTransformConcat(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransformconcat(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransformconcat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransformconcat%28_%3A_%3A%29.json'
content_hash: 'sha256:7232f57bf2c9225d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformConcat(_:_:)

<sub>Function</sub>

Returns an affine transformation matrix constructed by combining two existing affine transforms.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformConcat(_ t1: CGAffineTransform, _ t2: CGAffineTransform) -> CGAffineTransform
```

## Parameters

- `t1` — The first affine transform.

- `t2` — The second affine transform. This affine transform is concatenated to the first affine transform.

## Return Value

A new affine transformation matrix. That is, t’ = t1*t2.

## Discussion

Concatenation combines two affine transformation matrices by multiplying them together. You might perform several concatenations in order to create a single affine transform that contains the cumulative effects of several transformations.

Note that matrix operations are not commutative—the order in which you concatenate matrices is important. That is, the result of multiplying matrix `t1` by matrix `t2` does not necessarily equal the result of multiplying matrix `t2` by matrix `t1`.

## See Also

### Modifying Affine Transformations

- [CGAffineTransformTranslate](<cgaffinetransformtranslate(______).md>) — Returns an affine transformation matrix constructed by translating an existing affine transform.
- [CGAffineTransformScale](<cgaffinetransformscale(______).md>) — Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [CGAffineTransformRotate](<cgaffinetransformrotate(____).md>) — Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [CGAffineTransformInvert](<cgaffinetransforminvert(__).md>) — Returns an affine transformation matrix constructed by inverting an existing affine transform.

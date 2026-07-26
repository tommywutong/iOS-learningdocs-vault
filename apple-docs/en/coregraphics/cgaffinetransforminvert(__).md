---
title: 'CGAffineTransformInvert(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransforminvert(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransforminvert(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransforminvert%28_%3A%29.json'
content_hash: 'sha256:436fc9a168932009'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformInvert(_:)

<sub>Function</sub>

Returns an affine transformation matrix constructed by inverting an existing affine transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformInvert(_ t: CGAffineTransform) -> CGAffineTransform
```

## Parameters

- `t` — An existing affine transform.

## Return Value

A new affine transformation matrix. If the affine transform passed in parameter `t` cannot be inverted, the affine transform is returned unchanged.

## Discussion

Inversion is generally used to provide reverse transformation of points within transformed objects. Given the coordinates (x,y), which have been transformed by a given matrix to new coordinates (x’,y’), transforming the coordinates (x’,y’) by the inverse matrix produces the original coordinates (x,y).

## See Also

### Modifying Affine Transformations

- [CGAffineTransformTranslate](<cgaffinetransformtranslate(______).md>) — Returns an affine transformation matrix constructed by translating an existing affine transform.
- [CGAffineTransformScale](<cgaffinetransformscale(______).md>) — Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [CGAffineTransformRotate](<cgaffinetransformrotate(____).md>) — Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [CGAffineTransformConcat](<cgaffinetransformconcat(____).md>) — Returns an affine transformation matrix constructed by combining two existing affine transforms.

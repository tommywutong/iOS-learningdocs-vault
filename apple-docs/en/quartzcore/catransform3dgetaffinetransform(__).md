---
title: 'CATransform3DGetAffineTransform(_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3dgetaffinetransform(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3dgetaffinetransform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3dgetaffinetransform%28_%3A%29.json'
content_hash: 'sha256:1618d9f738c14f3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DGetAffineTransform(_:)

<sub>Function</sub>

Returns the affine transform represented by `t`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DGetAffineTransform(_ t: CATransform3D) -> CGAffineTransform
```

## Discussion

If `t` can not be exactly represented as an affine transform, the return value is undefined.

## See Also

### Converting to and from Core Graphics Affine Transforms

- [CATransform3DMakeAffineTransform](<catransform3dmakeaffinetransform(__).md>) — Returns a transform with the same effect as affine transform `m`.

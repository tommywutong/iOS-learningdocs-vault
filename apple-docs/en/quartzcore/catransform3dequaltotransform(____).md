---
title: 'CATransform3DEqualToTransform(_:_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3dequaltotransform(_:_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3dequaltotransform(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3dequaltotransform%28_%3A_%3A%29.json'
content_hash: 'sha256:4cd93f7af4abc270'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DEqualToTransform(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether the two transforms are exactly equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DEqualToTransform(_ a: CATransform3D, _ b: CATransform3D) -> Bool
```

## Return Value

[true](../swift/true.md) if `a` and `b` are exactly equal, otherwise [false](../swift/false.md).

## See Also

### Determining Transform Properties

- [CATransform3DIsAffine](<catransform3disaffine(__).md>) — Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.
- [CATransform3DIsIdentity](<catransform3disidentity(__).md>) — Returns a Boolean value that indicates whether the transform is the identity transform.

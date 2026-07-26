---
title: 'CATransform3DIsIdentity(_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3disidentity(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3disidentity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3disidentity%28_%3A%29.json'
content_hash: 'sha256:8442c30b729652b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DIsIdentity(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether the transform is the identity transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DIsIdentity(_ t: CATransform3D) -> Bool
```

## Return Value

[true](../swift/true.md) if `t` is the identity transform, otherwise [false](../swift/false.md).

## See Also

### Determining Transform Properties

- [CATransform3DIsAffine](<catransform3disaffine(__).md>) — Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.
- [CATransform3DEqualToTransform](<catransform3dequaltotransform(____).md>) — Returns a Boolean value that indicates whether the two transforms are exactly equal.

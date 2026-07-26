---
title: 'CATransform3DIsAffine(_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3disaffine(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3disaffine(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3disaffine%28_%3A%29.json'
content_hash: 'sha256:a1ba6e50416865aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DIsAffine(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DIsAffine(_ t: CATransform3D) -> Bool
```

## Discussion

Returns [true](../swift/true.md) if `t` can be exactly represented by an affine transform.

## See Also

### Determining Transform Properties

- [CATransform3DIsIdentity](<catransform3disidentity(__).md>) — Returns a Boolean value that indicates whether the transform is the identity transform.
- [CATransform3DEqualToTransform](<catransform3dequaltotransform(____).md>) — Returns a Boolean value that indicates whether the two transforms are exactly equal.

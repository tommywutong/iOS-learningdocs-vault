---
title: 'CATransform3DMakeRotation(_:_:_:_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3dmakerotation(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3dmakerotation(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3dmakerotation%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:446c6353366e86c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DMakeRotation(_:_:_:_:)

<sub>Function</sub>

Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DMakeRotation(_ angle: CGFloat, _ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> CATransform3D
```

## Discussion

If the vector has length zero, this function returns the identity transform.

## See Also

### Creating Transforms

- [CATransform3DMakeTranslation](<catransform3dmaketranslation(______).md>) — Returns a transform that translates by `(tx, ty, tz)`.
- [CATransform3DMakeScale](<catransform3dmakescale(______).md>) — Returns a transform that scales by `(sx, sy, sz)`.

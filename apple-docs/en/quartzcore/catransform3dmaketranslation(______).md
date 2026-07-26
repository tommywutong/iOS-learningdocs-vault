---
title: 'CATransform3DMakeTranslation(_:_:_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3dmaketranslation(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3dmaketranslation(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3dmaketranslation%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:064b03a04eeb8f0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DMakeTranslation(_:_:_:)

<sub>Function</sub>

Returns a transform that translates by `(tx, ty, tz)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DMakeTranslation(_ tx: CGFloat, _ ty: CGFloat, _ tz: CGFloat) -> CATransform3D
```

## Discussion

`t =  [1 0 0 0; 0 1 0 0; 0 0 1 0; tx ty tz 1].`

## See Also

### Creating Transforms

- [CATransform3DMakeScale](<catransform3dmakescale(______).md>) — Returns a transform that scales by `(sx, sy, sz)`.
- [CATransform3DMakeRotation](<catransform3dmakerotation(________).md>) — Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.

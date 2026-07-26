---
title: 'CATransform3DRotate(_:_:_:_:_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3drotate(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3drotate(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3drotate%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:70ebdc1b36ac5c6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DRotate(_:_:_:_:_:)

<sub>Function</sub>

Rotates `t` by `angle` radians about the vector `(x, y, z)` and returns the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DRotate(_ t: CATransform3D, _ angle: CGFloat, _ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> CATransform3D
```

## Discussion

If the vector has zero length, the behavior is undefined: `t` = `rotation(angle, x, y, z) * t`.

## See Also

### Chaining Transforms

- [CATransform3DConcat](<catransform3dconcat(____).md>) — Concatenates `b` to `a` and returns the result: `t = a * b`.
- [CATransform3DTranslate](<catransform3dtranslate(________).md>) — Translates `t` by `(tx, ty, tz)` and returns the result: `t` `= translate(tx, ty, tz) * t`.
- [CATransform3DScale](<catransform3dscale(________).md>) — Scales `t` by `(sx, sy, sz)` and returns the result: `t = scale(sx, sy, sz) * t`.

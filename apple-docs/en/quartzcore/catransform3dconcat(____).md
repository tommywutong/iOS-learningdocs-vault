---
title: 'CATransform3DConcat(_:_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3dconcat(_:_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3dconcat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3dconcat%28_%3A_%3A%29.json'
content_hash: 'sha256:978cc1e1fd2aaaf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DConcat(_:_:)

<sub>Function</sub>

Concatenates `b` to `a` and returns the result: `t = a * b`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DConcat(_ a: CATransform3D, _ b: CATransform3D) -> CATransform3D
```

## See Also

### Chaining Transforms

- [CATransform3DTranslate](<catransform3dtranslate(________).md>) — Translates `t` by `(tx, ty, tz)` and returns the result: `t` `= translate(tx, ty, tz) * t`.
- [CATransform3DScale](<catransform3dscale(________).md>) — Scales `t` by `(sx, sy, sz)` and returns the result: `t = scale(sx, sy, sz) * t`.
- [CATransform3DRotate](<catransform3drotate(__________).md>) — Rotates `t` by `angle` radians about the vector `(x, y, z)` and returns the result.

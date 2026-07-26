---
title: 'CATransform3DScale(_:_:_:_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3dscale(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3dscale(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3dscale%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:926e6bbcc334b5c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DScale(_:_:_:_:)

<sub>Function</sub>

Scales `t` by `(sx, sy, sz)` and returns the result: `t = scale(sx, sy, sz) * t`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DScale(_ t: CATransform3D, _ sx: CGFloat, _ sy: CGFloat, _ sz: CGFloat) -> CATransform3D
```

## See Also

### Chaining Transforms

- [CATransform3DConcat](<catransform3dconcat(____).md>) — Concatenates `b` to `a` and returns the result: `t = a * b`.
- [CATransform3DTranslate](<catransform3dtranslate(________).md>) — Translates `t` by `(tx, ty, tz)` and returns the result: `t` `= translate(tx, ty, tz) * t`.
- [CATransform3DRotate](<catransform3drotate(__________).md>) — Rotates `t` by `angle` radians about the vector `(x, y, z)` and returns the result.

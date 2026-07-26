---
title: rollAngle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, visionOS 1.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovergesturerecognizer/rollangle
source_url: 'https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/rollangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovergesturerecognizer/rollangle.json'
content_hash: 'sha256:f4bb162b1de01720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverGestureRecognizer](../uihovergesturerecognizer.md)

# rollAngle

<sub>Instance Property</sub>

A value that represents the current barrel-roll angle of Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var rollAngle: CGFloat { get }
```

## Discussion

For models of Apple Pencil that don’t support barrel-roll angle data, the value of this property is `0`.

## See Also

### Supporting Apple Pencil hover

- [altitudeAngle](altitudeangle.md) — A value that represents the altitude angle of the hovering pointing device.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [zOffset](zoffset.md) — A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.

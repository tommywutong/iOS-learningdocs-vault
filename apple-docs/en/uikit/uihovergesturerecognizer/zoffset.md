---
title: zOffset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovergesturerecognizer/zoffset
source_url: 'https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/zoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovergesturerecognizer/zoffset.json'
content_hash: 'sha256:20a3221571316c62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverGestureRecognizer](../uihovergesturerecognizer.md)

# zOffset

<sub>Instance Property</sub>

A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var zOffset: CGFloat { get }
```

## Discussion

This value is `1` at the maximum distance from the screen and approaches `0` as the pointing device gets closer to the screen. This value is `0` for devices that don’t support [zOffset](zoffset.md).

For example, a drawing app might use the value of this property to generate a preview that indicates where a hovering Apple Pencil touches down on an iPad screen. For more information, see [Adopting hover support for Apple Pencil](../adopting-hover-support-for-apple-pencil.md).

## See Also

### Supporting Apple Pencil hover

- [altitudeAngle](altitudeangle.md) — A value that represents the altitude angle of the hovering pointing device.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.

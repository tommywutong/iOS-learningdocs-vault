---
title: altitudeAngle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovergesturerecognizer/altitudeangle
source_url: 'https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/altitudeangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovergesturerecognizer/altitudeangle.json'
content_hash: 'sha256:f0fc6565fd9c0e56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverGestureRecognizer](../uihovergesturerecognizer.md)

# altitudeAngle

<sub>Instance Property</sub>

A value that represents the altitude angle of the hovering pointing device.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var altitudeAngle: CGFloat { get }
```

## Discussion

This value is `0` for devices that don’t support altitude.

## See Also

### Supporting Apple Pencil hover

- [- azimuthAngleInView:](<azimuthangle(in_).md>) — A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
- [zOffset](zoffset.md) — A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.

---
title: 'azimuthAngle(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uihovergesturerecognizer/azimuthangle(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/azimuthangle(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovergesturerecognizer/azimuthangle%28in%3A%29.json'
content_hash: 'sha256:e35055d899ec926a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverGestureRecognizer](../uihovergesturerecognizer.md)

# azimuthAngle(in:)

<sub>Instance Method</sub>

A value that represents the azimuth angle of the hovering pointing device in the specified view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func azimuthAngle(in view: UIView?) -> CGFloat
```

## Parameters

- `view` — The view the angle is relative to.

## Return Value

A [CGFloat](../../corefoundation/cgfloat-swift.struct.md) that represents the azimuth angle of the hovering pointing device.

## Discussion

If the specified view is `nil`, the method returns the azimuth angle of the hovering pointing device in the gesture recognizer’s window.

This method returns `0` for devices that don’t support azimuth.

## See Also

### Supporting Apple Pencil hover

- [altitudeAngle](altitudeangle.md) — A value that represents the altitude angle of the hovering pointing device.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
- [zOffset](zoffset.md) — A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.

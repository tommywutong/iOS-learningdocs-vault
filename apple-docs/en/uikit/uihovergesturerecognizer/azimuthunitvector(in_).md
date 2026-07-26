---
title: 'azimuthUnitVector(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uihovergesturerecognizer/azimuthunitvector(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/azimuthunitvector(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovergesturerecognizer/azimuthunitvector%28in%3A%29.json'
content_hash: 'sha256:2707876c5a81ee51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverGestureRecognizer](../uihovergesturerecognizer.md)

# azimuthUnitVector(in:)

<sub>Instance Method</sub>

A value that represents the azimuth unit vector of the hovering pointing device in the specified view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func azimuthUnitVector(in view: UIView?) -> CGVector
```

## Parameters

- `view` — The view the vector is relative to.

## Return Value

A [CGVector](../../corefoundation/cgvector.md) that represents the azimuth unit vector of the hovering pointing device.

## Discussion

If the specified view is `nil`, the method returns the azimuth unit vector of the hovering pointing device in the gesture recognizer’s window.

This method returns an empty vector for devices that don’t support azimuth.

## See Also

### Supporting Apple Pencil hover

- [altitudeAngle](altitudeangle.md) — A value that represents the altitude angle of the hovering pointing device.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
- [zOffset](zoffset.md) — A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.

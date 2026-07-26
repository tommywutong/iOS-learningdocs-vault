---
title: 'init(controlPoint1:controlPoint2:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicubictimingparameters/init(controlpoint1:controlpoint2:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicubictimingparameters/init(controlpoint1:controlpoint2:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicubictimingparameters/init%28controlpoint1%3Acontrolpoint2%3A%29.json'
content_hash: 'sha256:1758b688237038e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICubicTimingParameters](../uicubictimingparameters.md)

# init(controlPoint1:controlPoint2:)

<sub>Initializer</sub>

Initializes the object with the specified control points for a cubic Bézier curve.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(controlPoint1 point1: CGPoint, controlPoint2 point2: CGPoint)
```

## Parameters

- `point1` — The first control point for the cubic Bézier timing curve. The x and y values of this point must be in the range `0.0` to `1.0`.

- `point2` — The second control point for the cubic Bézier timing curve. The x and y values of this point must be in the range `0.0` to `1.0`.

## Return Value

An initialized timing parameter object or `nil` if the object could not be created.

## Discussion

Use this method to initialize the timing curve with a custom cubic Bézier curve. The curve consists of a line whose starting point is (0, 0), whose end point is (1, 1), and whose shape is defined by `point1` and `point2`.

## See Also

### Initializing a cubic timing parameters object

- [- init](<init().md>) — Initializes the object with the system’s default timing curve.
- [- initWithAnimationCurve:](<init(animationcurve_).md>) — Initializes the object with the specified UIKit timing curve.
- [- initWithCoder:](<init(coder_).md>) — Creates a timing parameters object from data in an unarchiver.

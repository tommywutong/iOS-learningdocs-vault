---
title: 'init(animationCurve:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicubictimingparameters/init(animationcurve:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicubictimingparameters/init(animationcurve:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicubictimingparameters/init%28animationcurve%3A%29.json'
content_hash: 'sha256:65f36b13a4ad7d1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICubicTimingParameters](../uicubictimingparameters.md)

# init(animationCurve:)

<sub>Initializer</sub>

Initializes the object with the specified UIKit timing curve.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(animationCurve curve: UIView.AnimationCurve)
```

## Parameters

- `curve` — The UIKit timing curve to use for the animations. You can specify a linear animation or an animation whose initial or final speed is slightly slower.

## Return Value

An initialized timing parameter object or `nil` if the object could not be created.

## Discussion

Use this method to create a timing curve that uses the standard UIKit timing curves such as [UIViewAnimationCurveEaseIn](../uiview/animationcurve/easein.md), [UIViewAnimationCurveEaseOut](../uiview/animationcurve/easeout.md), [UIViewAnimationCurveEaseInOut](../uiview/animationcurve/easeinout.md), or [UIViewAnimationCurveLinear](../uiview/animationcurve/linear.md).

## See Also

### Initializing a cubic timing parameters object

- [- init](<init().md>) — Initializes the object with the system’s default timing curve.
- [- initWithControlPoint1:controlPoint2:](<init(controlpoint1_controlpoint2_).md>) — Initializes the object with the specified control points for a cubic Bézier curve.
- [- initWithCoder:](<init(coder_).md>) — Creates a timing parameters object from data in an unarchiver.

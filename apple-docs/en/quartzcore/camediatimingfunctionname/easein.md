---
title: easeIn
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatimingfunctionname/easein
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunctionname/easein'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunctionname/easein.json'
content_hash: 'sha256:7ff0261def9e6c2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFunctionName](../camediatimingfunctionname.md)

# easeIn

<sub>Type Property</sub>

Ease-in pacing, which causes an animation to begin slowly and then speed up as it progresses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let easeIn: CAMediaTimingFunctionName
```

## Discussion

This is a Bézier timing function with the control points (0.42,0.0) and (1.0,1.0).

The following code shows how to create a basic animation object using ease-in interpolation.

```swift
 let verticalAnimation = CABasicAnimation(keyPath: "position.y")
 verticalAnimation.fromValue = 310
 verticalAnimation.toValue = 10
 verticalAnimation.timingFunction = CAMediaTimingFunction(name: kCAMediaTimingFunctionEaseIn)
```

A layer animated with the animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Path taken using ease-in timing function](../../../../attachments/b82af6bc9071639def1b44f0e86d73b1/media-2776814@2x.png)

## See Also

### Constants

- [kCAMediaTimingFunctionLinear](linear.md) — Linear pacing, which causes an animation to occur evenly over its duration.
- [kCAMediaTimingFunctionEaseOut](easeout.md) — Ease-out pacing, which causes an animation to begin quickly and then slow as it progresses.
- [kCAMediaTimingFunctionEaseInEaseOut](easeineaseout.md) — Ease-in-ease-out pacing, which causes an animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [kCAMediaTimingFunctionDefault](default.md) — The system default timing function. Use this function to ensure that the timing of your animations matches that of most system animations.

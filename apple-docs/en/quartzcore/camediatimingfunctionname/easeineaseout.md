---
title: easeInEaseOut
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatimingfunctionname/easeineaseout
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunctionname/easeineaseout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunctionname/easeineaseout.json'
content_hash: 'sha256:552c86ade04160e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFunctionName](../camediatimingfunctionname.md)

# easeInEaseOut

<sub>Type Property</sub>

Ease-in-ease-out pacing, which causes an animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let easeInEaseOut: CAMediaTimingFunctionName
```

## Discussion

This is a Bézier timing function with the control points (0.42,0.0) and (0.58,1.0).

The following code shows how to create a basic animation object using ease-in-ease-out interpolation.

```swift
let verticalAnimation = CABasicAnimation(keyPath: "position.y")  
verticalAnimation.fromValue = 310  
verticalAnimation.toValue = 10  
verticalAnimation.timingFunction = CAMediaTimingFunction(name: kCAMediaTimingFunctionEaseInEaseOut)
```

A layer animated with the animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Path taken using ease-in-ease-out timing function](../../../../attachments/8503fdf3db9809be5465103752d0914b/media-2776818@2x.png)

## See Also

### Constants

- [kCAMediaTimingFunctionLinear](linear.md) — Linear pacing, which causes an animation to occur evenly over its duration.
- [kCAMediaTimingFunctionEaseIn](easein.md) — Ease-in pacing, which causes an animation to begin slowly and then speed up as it progresses.
- [kCAMediaTimingFunctionEaseOut](easeout.md) — Ease-out pacing, which causes an animation to begin quickly and then slow as it progresses.
- [kCAMediaTimingFunctionDefault](default.md) — The system default timing function. Use this function to ensure that the timing of your animations matches that of most system animations.

---
title: 'animationDidStop(_:finished:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caanimationdelegate/animationdidstop(_:finished:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimationdelegate/animationdidstop(_:finished:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimationdelegate/animationdidstop%28_%3Afinished%3A%29.json'
content_hash: 'sha256:c89064d4c6665074'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimationDelegate](../caanimationdelegate.md)

# animationDidStop(_:finished:)

<sub>Instance Method</sub>

Tells the delegate the animation has ended.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func animationDidStop(_ anim: CAAnimation, finished flag: Bool)
```

## Parameters

- `anim` — The [CAAnimation](../caanimation.md) object that has ended.

- `flag` — A flag indicating whether the animation has completed by reaching the end of its duration.

## Discussion

The animation may have ended because it has completed its active duration or because it has been removed from the layer it is attached to. `flag` is true if the animation reached the end of its duration without being removed.

## See Also

### Customizing Start and Stop Times

- [- animationDidStart:](<animationdidstart(__).md>) — Tells the delegate the animation has started.

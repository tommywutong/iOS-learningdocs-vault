---
title: 'animationDidStart(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caanimationdelegate/animationdidstart(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimationdelegate/animationdidstart(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimationdelegate/animationdidstart%28_%3A%29.json'
content_hash: 'sha256:97f35e7e7a1bc0ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimationDelegate](../caanimationdelegate.md)

# animationDidStart(_:)

<sub>Instance Method</sub>

Tells the delegate the animation has started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func animationDidStart(_ anim: CAAnimation)
```

## Parameters

- `anim` — The [CAAnimation](../caanimation.md) object that has started.

## See Also

### Customizing Start and Stop Times

- [- animationDidStop:finished:](<animationdidstop(__finished_).md>) — Tells the delegate the animation has ended.

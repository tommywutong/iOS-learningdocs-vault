---
title: speed
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatiming/speed
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatiming/speed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatiming/speed.json'
content_hash: 'sha256:7c938b58a7eca07c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTiming](../camediatiming.md)

# speed

<sub>Instance Property</sub>

Specifies how time is mapped to receiver’s time space from the parent time space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var speed: Float { get set }
```

## Discussion

For example, if `speed` is 2.0 local time progresses twice as fast as parent time. Defaults to 1.0.

## See Also

### Duration and Speed

- [duration](duration.md) — Specifies the basic duration of the animation, in seconds.

---
title: repeatCount
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatiming/repeatcount
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatiming/repeatcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatiming/repeatcount.json'
content_hash: 'sha256:b8370d7c972dde21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTiming](../camediatiming.md)

# repeatCount

<sub>Instance Property</sub>

Determines the number of times the animation will repeat.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var repeatCount: Float { get set }
```

## Discussion

May be fractional. If the `repeatCount` is 0, it is ignored. Defaults to 0. If both [repeatDuration](repeatduration.md) and [repeatCount](repeatcount.md) are specified the behavior is undefined.

Setting this property to [greatestFiniteMagnitude](../../swift/float/greatestfinitemagnitude.md) will cause the animation to repeat forever.

## See Also

### Repeating Animations

- [repeatDuration](repeatduration.md) — Determines how many seconds the animation will repeat for.

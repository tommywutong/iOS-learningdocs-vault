---
title: repeatDuration
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatiming/repeatduration
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatiming/repeatduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatiming/repeatduration.json'
content_hash: 'sha256:a73f509c1a51d966'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTiming](../camediatiming.md)

# repeatDuration

<sub>Instance Property</sub>

Determines how many seconds the animation will repeat for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var repeatDuration: CFTimeInterval { get set }
```

## Discussion

Defaults to 0. If the `repeatDuration` is 0, it is ignored. If both [repeatDuration](repeatduration.md) and [repeatCount](repeatcount.md) are specified the behavior is undefined.

## See Also

### Repeating Animations

- [repeatCount](repeatcount.md) — Determines the number of times the animation will repeat.

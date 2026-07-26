---
title: autoreverses
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatiming/autoreverses
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatiming/autoreverses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatiming/autoreverses.json'
content_hash: 'sha256:927ebef9ad592925'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTiming](../camediatiming.md)

# autoreverses

<sub>Instance Property</sub>

Determines if the receiver plays in the reverse upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var autoreverses: Bool { get set }
```

## Discussion

When [true](../../swift/true.md), the receiver plays backwards after playing forwards. Defaults to [false](../../swift/false.md).

## See Also

### Playback Modes

- [fillMode](fillmode.md) — Determines if the receiver’s presentation is frozen or removed once its active duration has completed.

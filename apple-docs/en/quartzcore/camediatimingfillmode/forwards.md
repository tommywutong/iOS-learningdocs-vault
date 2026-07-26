---
title: forwards
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatimingfillmode/forwards
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfillmode/forwards'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfillmode/forwards.json'
content_hash: 'sha256:572e8b2d53c47123'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFillMode](../camediatimingfillmode.md)

# forwards

<sub>Type Property</sub>

The receiver remains visible in its final state when the animation is completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let forwards: CAMediaTimingFillMode
```

## See Also

### Constants

- [kCAFillModeRemoved](removed.md) — The receiver is removed from the presentation when the animation is completed.
- [kCAFillModeBackwards](backwards.md) — The receiver clamps values before zero to zero when the animation is completed.
- [kCAFillModeBoth](both.md) — The receiver clamps values at both ends of the object’s time space

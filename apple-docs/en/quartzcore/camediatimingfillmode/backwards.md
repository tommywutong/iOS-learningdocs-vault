---
title: backwards
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatimingfillmode/backwards
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfillmode/backwards'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfillmode/backwards.json'
content_hash: 'sha256:5cbe16cfe61a1e78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFillMode](../camediatimingfillmode.md)

# backwards

<sub>Type Property</sub>

The receiver clamps values before zero to zero when the animation is completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let backwards: CAMediaTimingFillMode
```

## See Also

### Constants

- [kCAFillModeRemoved](removed.md) — The receiver is removed from the presentation when the animation is completed.
- [kCAFillModeForwards](forwards.md) — The receiver remains visible in its final state when the animation is completed.
- [kCAFillModeBoth](both.md) — The receiver clamps values at both ends of the object’s time space

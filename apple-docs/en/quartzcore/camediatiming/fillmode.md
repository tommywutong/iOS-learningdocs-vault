---
title: fillMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatiming/fillmode
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatiming/fillmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatiming/fillmode.json'
content_hash: 'sha256:cc23dc80bb13cf86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTiming](../camediatiming.md)

# fillMode

<sub>Instance Property</sub>

Determines if the receiver’s presentation is frozen or removed once its active duration has completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fillMode: CAMediaTimingFillMode { get set }
```

## Discussion

The possible values are described in [Fill Modes](../fill-modes.md). The default is [kCAFillModeRemoved](../camediatimingfillmode/removed.md).

## See Also

### Playback Modes

- [autoreverses](autoreverses.md) — Determines if the receiver plays in the reverse upon completion.

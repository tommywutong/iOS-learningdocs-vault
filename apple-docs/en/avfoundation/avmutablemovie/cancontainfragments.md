---
title: canContainFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/cancontainfragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/cancontainfragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/cancontainfragments.json'
content_hash: 'sha256:f02e65b9f80fd709'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# canContainFragments

<sub>Instance Property</sub>

A Boolean value that indicates whether you can extend the asset by fragments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var canContainFragments: Bool { get }
```

## Discussion

For QuickTime movie files and MPEG-4 files, the value is [true](../../swift/true.md) if an `mvex` box is present in the `moov` box. For those types, the `mvex` box signals the possible presence of later `moof` boxes.

## See Also

### Determining fragment support

- [containsFragments](containsfragments.md) — A Boolean value that indicates whether at least one movie fragment extends the asset.
- [overallDurationHint](overalldurationhint.md) — The total duration of fragments that currently exist, or may exist in the future.

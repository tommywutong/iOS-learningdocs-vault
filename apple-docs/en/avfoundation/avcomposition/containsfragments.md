---
title: containsFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/containsfragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/containsfragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/containsfragments.json'
content_hash: 'sha256:cb23eaefe2f1832b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# containsFragments

<sub>Instance Property</sub>

A Boolean value that indicates whether at least one movie fragment extends the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var containsFragments: Bool { get }
```

## Discussion

For QuickTime movie files and MPEG-4 files, the value is [true](../../swift/true.md) if [canContainFragments](../avasset/cancontainfragments.md) is [true](../../swift/true.md) and at least one `moof` box is present after the `moov` box.

## See Also

### Determining fragment support

- [canContainFragments](cancontainfragments.md) — A Boolean value that indicates whether you can extend the asset by fragments.
- [overallDurationHint](overalldurationhint.md) — The total duration of fragments that currently exist, or may exist in the future.

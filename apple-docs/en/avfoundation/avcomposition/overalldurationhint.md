---
title: overallDurationHint
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.2+, iPadOS 10.2+, Mac Catalyst 13.1+, macOS 10.12.2+, tvOS 10.2+, visionOS 1.0+, watchOS 3.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/overalldurationhint
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/overalldurationhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/overalldurationhint.json'
content_hash: 'sha256:6048b38978a65e1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# overallDurationHint

<sub>Instance Property</sub>

The total duration of fragments that currently exist, or may exist in the future.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var overallDurationHint: CMTime { get }
```

## Discussion

For QuickTime movie files and MPEG-4 files, the asset retrieves this value from the `mehd` box of the `mvex` box, if present. If no total fragment duration hint is available, the value of this property is [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Determining fragment support

- [canContainFragments](cancontainfragments.md) — A Boolean value that indicates whether you can extend the asset by fragments.
- [containsFragments](containsfragments.md) — A Boolean value that indicates whether at least one movie fragment extends the asset.

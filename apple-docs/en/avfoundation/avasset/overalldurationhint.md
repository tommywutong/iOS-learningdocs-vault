---
title: overallDurationHint
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.2+（16.0 起废弃）, iPadOS 10.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.12.2+（13.0 起废弃）, tvOS 10.2+（16.0 起废弃）, watchOS 3.2+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/overalldurationhint
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/overalldurationhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/overalldurationhint.json'
content_hash: 'sha256:8a7e1dd2ad386193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# overallDurationHint

<sub>Instance Property</sub>

The total duration of fragments that currently exist, or may exist in the future.

> [!warning] Deprecated
> Load the value of [overallDurationHint](../avpartialasyncproperty/overalldurationhint.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var overallDurationHint: CMTime { get }
```

## Discussion

For QuickTime movie files and MPEG-4 files, the asset retrieves this value from the `mehd` box of the `mvex` box, if present. If no total fragment duration hint is available, the value of this property is [invalid](../../coremedia/cmtime/invalid.md).

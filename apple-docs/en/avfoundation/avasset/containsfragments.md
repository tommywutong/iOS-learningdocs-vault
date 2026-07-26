---
title: containsFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（16.0 起废弃）, iPadOS 9.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/containsfragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/containsfragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/containsfragments.json'
content_hash: 'sha256:a0e5290a5dcc004f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# containsFragments

<sub>Instance Property</sub>

A Boolean value that indicates whether at least one movie fragment extends the asset.

> [!warning] Deprecated
> Load the value of [containsFragments](../avpartialasyncproperty/containsfragments.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var containsFragments: Bool { get }
```

## Discussion

For QuickTime movie files and MPEG-4 files, the value is [true](../../swift/true.md) if [canContainFragments](cancontainfragments.md) is [true](../../swift/true.md) and at least one `moof` box is present after the `moov` box.

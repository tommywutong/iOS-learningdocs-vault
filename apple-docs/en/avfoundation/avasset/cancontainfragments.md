---
title: canContainFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（16.0 起废弃）, iPadOS 9.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/cancontainfragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/cancontainfragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/cancontainfragments.json'
content_hash: 'sha256:a1771fbb8e1f5978'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# canContainFragments

<sub>Instance Property</sub>

A Boolean value that indicates whether you can extend the asset by fragments.

> [!warning] Deprecated
> Load the value of [canContainFragments](../avpartialasyncproperty/cancontainfragments.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var canContainFragments: Bool { get }
```

## Discussion

For QuickTime movie files and MPEG-4 files, the value is [true](../../swift/true.md) if an `mvex` box is present in the `moov` box. For those types, the `mvex` box signals the possible presence of later `moof` boxes.

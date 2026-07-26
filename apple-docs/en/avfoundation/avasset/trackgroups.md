---
title: trackGroups
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（16.0 起废弃）, iPadOS 7.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.9+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/trackgroups
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/trackgroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/trackgroups.json'
content_hash: 'sha256:b38a44e98baad9ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# trackGroups

<sub>Instance Property</sub>

The track groups an asset contains.

> [!warning] Deprecated
> Load the value of [trackGroups](../avpartialasyncproperty/trackgroups.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var trackGroups: [AVAssetTrackGroup] { get }
```

## Discussion

This value is an empty array if the asset has no track groups.

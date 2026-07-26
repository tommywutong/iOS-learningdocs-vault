---
title: minimumTimeOffsetFromLive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS 13.0+（16.0 起废弃）, watchOS 6.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/minimumtimeoffsetfromlive
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/minimumtimeoffsetfromlive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/minimumtimeoffsetfromlive.json'
content_hash: 'sha256:3a1f04828cf049be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# minimumTimeOffsetFromLive

<sub>Instance Property</sub>

A time value that indicates how closely playback follows the latest live stream content.

> [!warning] Deprecated
> Load the value of [minimumTimeOffsetFromLive](../avpartialasyncproperty/minimumtimeoffsetfromlive.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var minimumTimeOffsetFromLive: CMTime { get }
```

## Discussion

This property value is only valid when working with live streaming content. For non-live assets, this property value is [invalid](../../coremedia/cmtime/invalid.md).

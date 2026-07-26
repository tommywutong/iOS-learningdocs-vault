---
title: isCompatibleWithAirPlayVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（16.0 起废弃）, iPadOS 9.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/iscompatiblewithairplayvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/iscompatiblewithairplayvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/iscompatiblewithairplayvideo.json'
content_hash: 'sha256:90bf435b68abad31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# isCompatibleWithAirPlayVideo

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset is compatible with AirPlay Video.

> [!warning] Deprecated
> Load the value of [isCompatibleWithAirPlayVideo](../avpartialasyncproperty/iscompatiblewithairplayvideo.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isCompatibleWithAirPlayVideo: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can play this asset’s content to an external AirPlay device, like an Apple TV.

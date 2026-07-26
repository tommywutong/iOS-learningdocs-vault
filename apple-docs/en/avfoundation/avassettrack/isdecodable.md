---
title: isDecodable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（16.0 起废弃）, iPadOS 11.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.13+（13.0 起废弃）, tvOS 11.0+（16.0 起废弃）, watchOS 4.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/isdecodable
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/isdecodable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/isdecodable.json'
content_hash: 'sha256:1fbd151f9b451319'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# isDecodable

<sub>Instance Property</sub>

A Boolean value that indicates whether the track is decodable in the current environment.

> [!warning] Deprecated
> Load the value of [isDecodable](../avpartialasyncproperty/isdecodable.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var isDecodable: Bool { get }
```

## Discussion

When this property is [true](../../swift/true.md), the system can decode the track, even if decoding may be too slow for real-time playback.

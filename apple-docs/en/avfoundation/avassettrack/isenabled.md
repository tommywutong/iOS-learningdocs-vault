---
title: isEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/isenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/isenabled.json'
content_hash: 'sha256:37ecd8528897c78f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the track’s container enables it.

> [!warning] Deprecated
> Load the value of [isEnabled](../avpartialasyncproperty/isenabled.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEnabled: Bool { get }
```

## Discussion

For file-based media, you can change its [enabled](../avplayeritemtrack/isenabled.md) presentation state using [AVPlayerItemTrack](../avplayeritemtrack.md).

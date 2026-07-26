---
title: nominalFrameRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/nominalframerate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/nominalframerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/nominalframerate.json'
content_hash: 'sha256:4ecd6b210fae9011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# nominalFrameRate

<sub>Instance Property</sub>

The frame rate of the track, in frames per second.

> [!warning] Deprecated
> Load the value of [nominalFrameRate](../avpartialasyncproperty/nominalframerate.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nominalFrameRate: Float { get }
```

## Discussion

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

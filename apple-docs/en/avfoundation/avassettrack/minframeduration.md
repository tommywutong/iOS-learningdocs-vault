---
title: minFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（16.0 起废弃）, iPadOS 7.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.10+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/minframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/minframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/minframeduration.json'
content_hash: 'sha256:7c4d8b211ca28182'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# minFrameDuration

<sub>Instance Property</sub>

The minimum duration of the track’s frames.

> [!warning] Deprecated
> Load the value of [minFrameDuration](../avpartialasyncproperty/minframeduration.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var minFrameDuration: CMTime { get }
```

## Discussion

A track’s minimum frame duration is the reciprocal of its maximum frame rate. For example, a video track with a maximum frame rate of 30 frames per second has a minimum frame duration of 1/30, or 0.033 seconds.

The value of this property is [invalid](../../coremedia/cmtime/invalid.md) if the track can’t calculate its minimum frame duration, or if it’s unknown.

---
title: preferredVolume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/preferredvolume
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/preferredvolume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/preferredvolume.json'
content_hash: 'sha256:735af93abe93451d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# preferredVolume

<sub>Instance Property</sub>

The track’s volume preference for playing its audible media.

> [!warning] Deprecated
> Load the value of [preferredVolume](../avpartialasyncproperty/preferredvolume-8q2yt.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredVolume: Float { get }
```

## Discussion

The preferred volume for an audio track is typically, but not always, `1.0`. For non-audible tracks, the value is `0.0`.

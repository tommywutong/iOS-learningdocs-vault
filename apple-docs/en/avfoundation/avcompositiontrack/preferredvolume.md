---
title: preferredVolume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/preferredvolume
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/preferredvolume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/preferredvolume.json'
content_hash: 'sha256:370716f162788f4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# preferredVolume

<sub>Instance Property</sub>

The track’s volume preference for playing its audible media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredVolume: Float { get }
```

## Discussion

The preferred volume for an audio track is typically, but not always, `1.0`. For non-audible tracks, the value is `0.0`.

## See Also

### Accessing audible characteristics

- [hasAudioSampleDependencies](hasaudiosampledependencies.md) — A Boolean value that indicates whether the track has sample dependencies.

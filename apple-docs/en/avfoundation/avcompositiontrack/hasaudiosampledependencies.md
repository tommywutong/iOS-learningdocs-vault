---
title: hasAudioSampleDependencies
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/hasaudiosampledependencies
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/hasaudiosampledependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/hasaudiosampledependencies.json'
content_hash: 'sha256:bcc35fbc9ba6a2ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# hasAudioSampleDependencies

<sub>Instance Property</sub>

A Boolean value that indicates whether the track has sample dependencies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasAudioSampleDependencies: Bool { get }
```

## Discussion

The value is always [false](../../swift/false.md) for nonaudible media.

## See Also

### Accessing audible characteristics

- [preferredVolume](preferredvolume.md) — The track’s volume preference for playing its audible media.

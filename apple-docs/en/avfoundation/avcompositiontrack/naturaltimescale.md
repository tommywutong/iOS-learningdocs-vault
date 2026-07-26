---
title: naturalTimeScale
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/naturaltimescale
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/naturaltimescale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/naturaltimescale.json'
content_hash: 'sha256:67137743808b664b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# naturalTimeScale

<sub>Instance Property</sub>

The natural time scale of the media that a track references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var naturalTimeScale: CMTimeScale { get }
```

## See Also

### Accessing temporal information

- [timeRange](timerange.md) — The time range of the track within the overall timeline of the asset.
- [estimatedDataRate](estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.
- [- samplePresentationTimeForTrackTime:](<samplepresentationtime(fortracktime_).md>) — Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

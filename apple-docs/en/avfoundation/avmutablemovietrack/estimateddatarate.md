---
title: estimatedDataRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/estimateddatarate
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/estimateddatarate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/estimateddatarate.json'
content_hash: 'sha256:cc20315b06bc0a8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# estimatedDataRate

<sub>Instance Property</sub>

The estimated data rate, in bits per second, of the media that the track references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var estimatedDataRate: Float { get }
```

## See Also

### Accessing temporal information

- [timeRange](timerange.md) — The time range of the track within the overall timeline of the asset.
- [timescale](timescale.md) — The time scale for tracks that contain the `moov` atom.
- [naturalTimeScale](naturaltimescale.md) — The natural time scale of the media that a track references.
- [- samplePresentationTimeForTrackTime:](<samplepresentationtime(fortracktime_).md>) — Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

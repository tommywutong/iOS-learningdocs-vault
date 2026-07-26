---
title: 'samplePresentationTime(forTrackTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/samplepresentationtime(fortracktime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/samplepresentationtime(fortracktime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/samplepresentationtime%28fortracktime%3A%29.json'
content_hash: 'sha256:2d6a4fdde8a67820'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# samplePresentationTime(forTrackTime:)

<sub>Instance Method</sub>

Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime
```

## Parameters

- `trackTime` — The track time for which to request the sample presentation time.

## Return Value

The sample presentation time corresponding to the specified time; otherwise [invalid](../../coremedia/cmtime/invalid.md) if the time is out of range.

## See Also

### Accessing temporal information

- [timeRange](timerange.md) — The time range of the track within the overall timeline of the asset.
- [timescale](timescale.md) — The time scale for tracks that contain the `moov` atom.
- [naturalTimeScale](naturaltimescale.md) — The natural time scale of the media that a track references.
- [estimatedDataRate](estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.

---
title: 'samplePresentationTime(forTrackTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcompositiontrack/samplepresentationtime(fortracktime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/samplepresentationtime(fortracktime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/samplepresentationtime%28fortracktime%3A%29.json'
content_hash: 'sha256:b298270b1f951281'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# samplePresentationTime(forTrackTime:)

<sub>Instance Method</sub>

Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

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
- [naturalTimeScale](naturaltimescale.md) — The natural time scale of the media that a track references.
- [estimatedDataRate](estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.

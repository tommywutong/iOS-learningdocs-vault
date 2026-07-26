---
title: preferredMediaChunkDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/preferredmediachunkduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/preferredmediachunkduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/preferredmediachunkduration.json'
content_hash: 'sha256:2aeb4a0a6efe5cfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# preferredMediaChunkDuration

<sub>Instance Property</sub>

The maximum duration to use for each chunk of sample data written to the file for file types that support media chunk duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var preferredMediaChunkDuration: CMTime { get set }
```

## Discussion

The total duration of the samples in a chunk can be no greater than the preferred chunk duration, or the duration of a single sample if the single sample’s duration is greater than the preferred chunk duration. The default media chunk duration is `1.0` second. Setting a negative or non-numeric value for the chunk duration will cause an error.

## See Also

### Accessing media chunks

- [preferredMediaChunkAlignment](preferredmediachunkalignment.md) — The boundary for media chunk alignment for file types that support media chunk alignment.
- [preferredMediaChunkSize](preferredmediachunksize.md) — The maximum size to use for each chunk of sample data written to the file for file types that support media chunk duration.

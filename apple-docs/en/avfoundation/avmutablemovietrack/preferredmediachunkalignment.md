---
title: preferredMediaChunkAlignment
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/preferredmediachunkalignment
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/preferredmediachunkalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/preferredmediachunkalignment.json'
content_hash: 'sha256:4592d4bee88fc322'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# preferredMediaChunkAlignment

<sub>Instance Property</sub>

The boundary for media chunk alignment for file types that support media chunk alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var preferredMediaChunkAlignment: Int { get set }
```

## Discussion

The default value is `0`, which indicates to use no padding should to achieve chunk alignment. Setting a negative chunk alignment value causes an error.

## See Also

### Accessing media chunks

- [preferredMediaChunkDuration](preferredmediachunkduration.md) — The maximum duration to use for each chunk of sample data written to the file for file types that support media chunk duration.
- [preferredMediaChunkSize](preferredmediachunksize.md) — The maximum size to use for each chunk of sample data written to the file for file types that support media chunk duration.

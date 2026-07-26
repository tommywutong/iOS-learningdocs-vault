---
title: isEmpty
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontracksegment/isempty
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontracksegment/isempty.json'
content_hash: 'sha256:a1ca082dc62cc80b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrackSegment](../avcompositiontracksegment.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value that indicates whether the segment is empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

An empty segment has a valid target time range, but its [sourceURL](sourceurl.md) value is `nil` and the source start time is [invalid](../../coremedia/cmtime/invalid.md). It doesn’t set values for its other properties.

## See Also

### Accessing segment properties

- [sourceURL](sourceurl.md) — A URL of the container file whose media this track segment presents.
- [sourceTrackID](sourcetrackid.md) — An identifier of a track in the container file whose media this track segment presents.

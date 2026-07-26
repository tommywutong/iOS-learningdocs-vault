---
title: sourceTrackID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontracksegment/sourcetrackid
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/sourcetrackid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontracksegment/sourcetrackid.json'
content_hash: 'sha256:3cce88694d3e261d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrackSegment](../avcompositiontracksegment.md)

# sourceTrackID

<sub>Instance Property</sub>

An identifier of a track in the container file whose media this track segment presents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sourceTrackID: CMPersistentTrackID { get }
```

## See Also

### Accessing segment properties

- [sourceURL](sourceurl.md) — A URL of the container file whose media this track segment presents.
- [empty](isempty.md) — A Boolean value that indicates whether the segment is empty.

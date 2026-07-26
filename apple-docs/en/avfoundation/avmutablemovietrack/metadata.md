---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/metadata.json'
content_hash: 'sha256:eebafafd2b211d30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# metadata

<sub>Instance Property</sub>

An array of metadata stored by the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var metadata: [AVMetadataItem] { get set }
```

## See Also

### Accessing metadata

- [commonMetadata](commonmetadata.md) — An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](availablemetadataformats.md) — An array of metadata formats available for the track.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns metadata items that a track contains for the specified format.

---
title: externalMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/externalmetadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/externalmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/externalmetadata.json'
content_hash: 'sha256:fdcb218ca047fdc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# externalMetadata

<sub>Instance Property</sub>

An array of additional metadata for the player item to supplement or replace an asset’s embedded metadata.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var externalMetadata: [AVMetadataItem] { get set }
```

## Discussion

[AVPlayerViewController](../../avkit/avplayerviewcontroller.md) supports displaying the following metadata identifiers:

- [AVMetadataCommonKeyTitle](../avmetadatakey/commonkeytitle.md)
- [AVMetadataIdentifieriTunesMetadataTrackSubTitle](../avmetadataidentifier/itunesmetadatatracksubtitle.md)
- [AVMetadataCommonIdentifierArtwork](../avmetadataidentifier/commonidentifierartwork.md)
- [AVMetadataCommonKeyDescription](../avmetadatakey/commonkeydescription.md)
- [AVMetadataiTunesMetadataKeyContentRating](../avmetadatakey/itunesmetadatakeycontentrating.md)
- [AVMetadataQuickTimeMetadataKeyGenre](../avmetadatakey/quicktimemetadatakeygenre.md)

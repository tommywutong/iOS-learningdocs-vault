---
title: timedMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（13.0 起废弃）, iPadOS 4.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritem/timedmetadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/timedmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/timedmetadata.json'
content_hash: 'sha256:e84004652d949a69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# timedMetadata

<sub>Instance Property</sub>

An array of the most recently encountered timed metadata.

> [!warning] Deprecated
> Use [AVPlayerItemMetadataOutput](../avplayeritemmetadataoutput.md) to access timed metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@MainActor var timedMetadata: [AVMetadataItem]? { get }
```

## Return Value

An array of [AVMetadataItem](../avmetadataitem.md) or `nil` if no metadata was found.

## Discussion

Prior to the player item loading its media, this property value is `nil`. You can key-value observe this property to monitor when metadata becomes available.

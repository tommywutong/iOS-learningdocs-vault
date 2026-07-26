---
title: availableMetadataFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-5p9xg
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-5p9xg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-5p9xg.json'
content_hash: 'sha256:e3a034fb9dc6ac82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# availableMetadataFormats

<sub>Type Property</sub>

An array of metadata formats available for the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading metadata

- [metadata](metadata-6e14c.md) — An array of metadata items for all metadata identifiers that have a value.
- [commonMetadata](commonmetadata-73m58.md) — An array of metadata items for all common metadata keys that have a value.
- [- loadMetadataForFormat:completionHandler:](<../avassettrack/loadmetadata(for_completionhandler_).md>) — Loads metadata items that a track contains for the specified format.

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
doc_path: /documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-4yiq8
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-4yiq8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-4yiq8.json'
content_hash: 'sha256:3c8d81654e8bafc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# availableMetadataFormats

<sub>Type Property</sub>

The formats of metadata that an asset contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading metadata

- [metadata](metadata-16qej.md) — The metadata items that an asset contains for all metadata identifiers.
- [commonMetadata](commonmetadata-3j3n4.md) — The metadata items that an asset contains for common metadata identifiers.
- [- loadMetadataForFormat:completionHandler:](<../avasset/loadmetadata(for_completionhandler_).md>) — Loads an array of metadata items that the asset contains for the specified format.
- [creationDate](creationdate.md) — A metadata item that indicates the creation date of an asset.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.

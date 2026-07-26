---
title: creationDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/creationdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/creationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/creationdate.json'
content_hash: 'sha256:eb4189a6ba9ca34f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# creationDate

<sub>Type Property</sub>

A metadata item that indicates the creation date of an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var creationDate: AVAsyncProperty<Root, AVMetadataItem?> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

If the asset stores a creation date in a form the system can convert to an [NSDate](../../foundation/nsdate.md), the metadata item’s [dateValue](../avmetadataitem/datevalue.md) property contains a valid date. Otherwise, the creation date is available only as a string that you retrieve by calling the metadata item’s [stringValue](../avmetadataitem/stringvalue.md) property.

This property may be `nil`.

## See Also

### Loading metadata

- [metadata](metadata-16qej.md) — The metadata items that an asset contains for all metadata identifiers.
- [commonMetadata](commonmetadata-3j3n4.md) — The metadata items that an asset contains for common metadata identifiers.
- [availableMetadataFormats](availablemetadataformats-4yiq8.md) — The formats of metadata that an asset contains.
- [- loadMetadataForFormat:completionHandler:](<../avasset/loadmetadata(for_completionhandler_).md>) — Loads an array of metadata items that the asset contains for the specified format.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.

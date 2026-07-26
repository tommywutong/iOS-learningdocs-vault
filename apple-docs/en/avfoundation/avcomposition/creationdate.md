---
title: creationDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/creationdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/creationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/creationdate.json'
content_hash: 'sha256:bee85ca0d0cc0b2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# creationDate

<sub>Instance Property</sub>

A metadata item that indicates the asset’s creation date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var creationDate: AVMetadataItem? { get }
```

## Discussion

If the asset contains metadata that the framework can convert to an [NSDate](../../foundation/nsdate.md), you can retrieve it from the metadata item using its [dateValue](../avmetadataitem/datevalue.md) property. Otherwise, you retrieve it as a string by using the metadata item’s [stringValue](../avmetadataitem/stringvalue.md) property.

This property value is `nil` if no creation date metadata exists.

## See Also

### Accessing metadata

- [metadata](metadata.md) — An array of metadata items for all metadata identifiers for which a value is available.
- [commonMetadata](commonmetadata.md) — The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](availablemetadataformats.md) — The metadata formats this asset contains.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns an array of metadata items from the container with the specified format.
- [lyrics](lyrics.md) — The lyrics of the asset in a language suitable for the current locale.

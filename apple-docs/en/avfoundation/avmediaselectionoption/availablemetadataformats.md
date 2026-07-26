---
title: availableMetadataFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/availablemetadataformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/availablemetadataformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/availablemetadataformats.json'
content_hash: 'sha256:68cc08ecf77d7043'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# availableMetadataFormats

<sub>Instance Property</sub>

The metadata formats that contain metadata associated with the option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var availableMetadataFormats: [String] { get }
```

## Discussion

The array contains `NSString` objects, each representing a metadata format that contains metadata associated with the option (for example, ID3, iTunes metadata, and so on).

## See Also

### Managing metadata

- [commonMetadata](commonmetadata.md) — An array of metadata items for each common metadata key for which a value is available.
- [- metadataForFormat:](<metadata(forformat_).md>) — Returns an array of metadata items—one for each metadata item in the container of a given format.

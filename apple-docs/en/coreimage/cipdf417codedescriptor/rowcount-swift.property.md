---
title: rowCount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipdf417codedescriptor/rowcount-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/rowcount-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipdf417codedescriptor/rowcount-swift.property.json'
content_hash: 'sha256:6b89ac6dca78b4f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md)

# rowCount

<sub>Instance Property</sub>

The number of rows in the PDF417 code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rowCount: Int { get }
```

## Discussion

Valid row count values are from 3 to 90.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [isCompact](iscompact-swift.property.md) — A boolean value telling if the PDF417 code is compact.
- [columnCount](columncount-swift.property.md) — The number of columns in the PDF417 code symbol.

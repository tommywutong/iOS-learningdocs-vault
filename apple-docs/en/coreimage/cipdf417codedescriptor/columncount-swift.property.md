---
title: columnCount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipdf417codedescriptor/columncount-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/columncount-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipdf417codedescriptor/columncount-swift.property.json'
content_hash: 'sha256:9b9c9a100b802fa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md)

# columnCount

<sub>Instance Property</sub>

The number of columns in the PDF417 code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var columnCount: Int { get }
```

## Discussion

Valid column count values are from 1 to 30. This count excluded the columns used to indicate the symbol structure.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [isCompact](iscompact-swift.property.md) — A boolean value telling if the PDF417 code is compact.
- [rowCount](rowcount-swift.property.md) — The number of rows in the PDF417 code symbol.

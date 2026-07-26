---
title: isCompact
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipdf417codedescriptor/iscompact-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/iscompact-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipdf417codedescriptor/iscompact-swift.property.json'
content_hash: 'sha256:509b18bf49d622c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md)

# isCompact

<sub>Instance Property</sub>

A boolean value telling if the PDF417 code is compact.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isCompact: Bool { get }
```

## Discussion

Compact PDF417 symbols have abbreviated right-side guard bars.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [rowCount](rowcount-swift.property.md) — The number of rows in the PDF417 code symbol.
- [columnCount](columncount-swift.property.md) — The number of columns in the PDF417 code symbol.

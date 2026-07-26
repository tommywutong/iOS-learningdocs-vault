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
doc_path: /documentation/coreimage/ciazteccodedescriptor/iscompact-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/iscompact-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodedescriptor/iscompact-swift.property.json'
content_hash: 'sha256:e45ce1b93b263451'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIAztecCodeDescriptor](../ciazteccodedescriptor.md)

# isCompact

<sub>Instance Property</sub>

A Boolean value telling if the Aztec code is compact.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isCompact: Bool { get }
```

## Discussion

Compact Aztec symbols use one-fewer ring in the central finder pattern than full-range Aztec symbols of the same number of data layers.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload that comprises the the Aztec code symbol.
- [layerCount](layercount-swift.property.md) — The number of data layers in the Aztec code symbol.
- [dataCodewordCount](datacodewordcount-swift.property.md) — The number of non-error-correction codewords carried by the Aztec code symbol.

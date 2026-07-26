---
title: layerCount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciazteccodedescriptor/layercount-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/layercount-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodedescriptor/layercount-swift.property.json'
content_hash: 'sha256:209bdbf170f8580c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIAztecCodeDescriptor](../ciazteccodedescriptor.md)

# layerCount

<sub>Instance Property</sub>

The number of data layers in the Aztec code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layerCount: Int { get }
```

## Discussion

Combined with [isCompact](iscompact-swift.property.md), the number of data layers determines the number of
modules in the Aztec Code symbol. Valid values range from 1 to 32. Compact symbols can have up to 4 data layers.

The number of data layers also determines the number of bits in each data codeword of the message carried by the Aztec Code symbol.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload that comprises the the Aztec code symbol.
- [isCompact](iscompact-swift.property.md) — A Boolean value telling if the Aztec code is compact.
- [dataCodewordCount](datacodewordcount-swift.property.md) — The number of non-error-correction codewords carried by the Aztec code symbol.

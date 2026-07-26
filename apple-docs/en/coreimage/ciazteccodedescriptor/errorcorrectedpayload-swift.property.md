---
title: errorCorrectedPayload
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciazteccodedescriptor/errorcorrectedpayload-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/errorcorrectedpayload-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodedescriptor/errorcorrectedpayload-swift.property.json'
content_hash: 'sha256:656f86ecac91eff8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIAztecCodeDescriptor](../ciazteccodedescriptor.md)

# errorCorrectedPayload

<sub>Instance Property</sub>

The error-corrected payload that comprises the the Aztec code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var errorCorrectedPayload: Data { get }
```

## Discussion

Aztec Codes are formally specified in ISO/IEC 24778:2008(E).

The error corrected payload consists of the 6-, 8-, 10-, or 12-bit message codewords produced at the end of the step described in section 7.3.1.2 “Formation of data codewords”, which exists immediately prior to adding error correction. These codewords have dummy bits inserted to ensure that an entire codeword isn’t all 0’s or all 1’s. Clients will need to remove these extra bits as part of interpreting the payload.

## See Also

### Examining a Descriptor

- [isCompact](iscompact-swift.property.md) — A Boolean value telling if the Aztec code is compact.
- [layerCount](layercount-swift.property.md) — The number of data layers in the Aztec code symbol.
- [dataCodewordCount](datacodewordcount-swift.property.md) — The number of non-error-correction codewords carried by the Aztec code symbol.

---
title: dataCodewordCount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciazteccodedescriptor/datacodewordcount-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/datacodewordcount-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodedescriptor/datacodewordcount-swift.property.json'
content_hash: 'sha256:3b611882903cbd85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIAztecCodeDescriptor](../ciazteccodedescriptor.md)

# dataCodewordCount

<sub>Instance Property</sub>

The number of non-error-correction codewords carried by the Aztec code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dataCodewordCount: Int { get }
```

## Discussion

Used to determine the level of error correction in conjunction with the number of data layers. Valid values are 1 to 2048. Compact symbols can have up to 64 message codewords.

> [!note] Note
> This value can exceed the number of message codewords allowed by the number of data layers in this symbol. In this case, the actual number of message codewords is 1024 fewer than this value and the message payload is to be interpreted in an application-defined manner.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload that comprises the the Aztec code symbol.
- [isCompact](iscompact-swift.property.md) — A Boolean value telling if the Aztec code is compact.
- [layerCount](layercount-swift.property.md) — The number of data layers in the Aztec code symbol.

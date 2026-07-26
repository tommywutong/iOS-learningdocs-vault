---
title: 'descriptorWithPayload:isCompact:layerCount:dataCodewordCount:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciazteccodedescriptor/descriptorwithpayload:iscompact:layercount:datacodewordcount:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/descriptorwithpayload:iscompact:layercount:datacodewordcount:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodedescriptor/descriptorwithpayload%3Aiscompact%3Alayercount%3Adatacodewordcount%3A.json'
content_hash: 'sha256:d11d9d397d1faed9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIAztecCodeDescriptor](../ciazteccodedescriptor.md)

# descriptorWithPayload:isCompact:layerCount:dataCodewordCount:

<sub>Type Method</sub>

Creates an Aztec code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) descriptorWithPayload:(NSData *) errorCorrectedPayload isCompact:(BOOL) isCompact layerCount:(NSInteger) layerCount dataCodewordCount:(NSInteger) dataCodewordCount;
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the Aztec code symbol.

- `isCompact` — A Boolean indicating whether or not the Aztec code is compact.

- `layerCount` — The number of layers in the Aztec code, from 1 to 32.

- `dataCodewordCount` — The number of codewords in the Aztec code, from 1 to 2048.

## Return Value

An autoreleased [CIAztecCodeDescriptor](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## See Also

### Creating a Descriptor

- [- initWithPayload:isCompact:layerCount:dataCodewordCount:](<init(payload_iscompact_layercount_datacodewordcount_).md>) — Initializes an Aztec code descriptor for the given payload and parameters.

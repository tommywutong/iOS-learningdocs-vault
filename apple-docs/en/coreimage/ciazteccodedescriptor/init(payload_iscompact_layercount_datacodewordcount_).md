---
title: 'init(payload:isCompact:layerCount:dataCodewordCount:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciazteccodedescriptor/init(payload:iscompact:layercount:datacodewordcount:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/init(payload:iscompact:layercount:datacodewordcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodedescriptor/init%28payload%3Aiscompact%3Alayercount%3Adatacodewordcount%3A%29.json'
content_hash: 'sha256:e5ba8847d0f4d2f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIAztecCodeDescriptor](../ciazteccodedescriptor.md)

# init(payload:isCompact:layerCount:dataCodewordCount:)

<sub>Initializer</sub>

Initializes an Aztec code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(payload errorCorrectedPayload: Data, isCompact: Bool, layerCount: Int, dataCodewordCount: Int)
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the Aztec code symbol.

- `isCompact` — A Boolean indicating whether or not the Aztec code is compact.

- `layerCount` — The number of layers in the Aztec code, from 1 to 32.

- `dataCodewordCount` — The number of codewords in the Aztec code, from 1 to 2048.

## Return Value

An initialized [CIAztecCodeDescriptor](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

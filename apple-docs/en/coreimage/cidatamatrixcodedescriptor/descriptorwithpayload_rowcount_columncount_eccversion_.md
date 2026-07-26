---
title: 'descriptorWithPayload:rowCount:columnCount:eccVersion:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cidatamatrixcodedescriptor/descriptorwithpayload:rowcount:columncount:eccversion:'
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/descriptorwithpayload:rowcount:columncount:eccversion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor/descriptorwithpayload%3Arowcount%3Acolumncount%3Aeccversion%3A.json'
content_hash: 'sha256:04745241059e1b47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)

# descriptorWithPayload:rowCount:columnCount:eccVersion:

<sub>Type Method</sub>

Creates a Data Matrix code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) descriptorWithPayload:(NSData *) errorCorrectedPayload rowCount:(NSInteger) rowCount columnCount:(NSInteger) columnCount eccVersion:(CIDataMatrixCodeECCVersion) eccVersion;
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the Data Matrix code symbol.

- `rowCount` — The number of rows in the Data Matrix code symbol.

- `columnCount` — The number of columns in the Data Matrix code symbol.

- `eccVersion` — The [ECCVersion](eccversion-swift.enum.md) for the Data Matrix code symbol.

## Return Value

An autoreleased [CIAztecCodeDescriptor](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## See Also

### Creating a Descriptor

- [- initWithPayload:rowCount:columnCount:eccVersion:](<init(payload_rowcount_columncount_eccversion_).md>) — Initializes a Data Matrix code descriptor for the given payload and parameters.

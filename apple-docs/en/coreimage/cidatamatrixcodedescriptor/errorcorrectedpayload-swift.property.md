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
doc_path: /documentation/coreimage/cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property.json'
content_hash: 'sha256:5db7463fac7dde7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)

# errorCorrectedPayload

<sub>Instance Property</sub>

The error-corrected payload containing the data encoded in the Data Matrix code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var errorCorrectedPayload: Data { get }
```

## Discussion

DataMatrix symbols are specified bn ISO/IEC 16022:2006(E). ECC 200-type symbols will always have an even number of rows and columns.

For ECC 200-type symbols, the phases of encoding data into a symbol are described in section 5.1 – Encode procedure overview. The error corrected payload comprises the de-interleaved bits of the message described at the end of Step 1: Data encodation.

## See Also

### Examining a Descriptor

- [rowCount](rowcount-swift.property.md) — The number of rows in the Data Matrix code symbol.
- [columnCount](columncount-swift.property.md) — The number of columns in the Data Matrix code symbol.
- [eccVersion](eccversion-swift.property.md) — The error correction version of the Data Matrix code symbol.

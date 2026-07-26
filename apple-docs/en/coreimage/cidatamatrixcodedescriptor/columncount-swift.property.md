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
doc_path: /documentation/coreimage/cidatamatrixcodedescriptor/columncount-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/columncount-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor/columncount-swift.property.json'
content_hash: 'sha256:d0040c67ac732d5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)

# columnCount

<sub>Instance Property</sub>

The number of columns in the Data Matrix code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var columnCount: Int { get }
```

## Discussion

Refer to ISO/IEC 16022:2006(E) for valid module row and column count combinations.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [rowCount](rowcount-swift.property.md) — The number of rows in the Data Matrix code symbol.
- [eccVersion](eccversion-swift.property.md) — The error correction version of the Data Matrix code symbol.

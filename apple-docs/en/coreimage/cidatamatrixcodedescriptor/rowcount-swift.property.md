---
title: rowCount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidatamatrixcodedescriptor/rowcount-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/rowcount-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor/rowcount-swift.property.json'
content_hash: 'sha256:3729031a13cf6c8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)

# rowCount

<sub>Instance Property</sub>

The number of rows in the Data Matrix code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rowCount: Int { get }
```

## Discussion

Refer to ISO/IEC 16022:2006(E) for valid module row and column count combinations.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [columnCount](columncount-swift.property.md) — The number of columns in the Data Matrix code symbol.
- [eccVersion](eccversion-swift.property.md) — The error correction version of the Data Matrix code symbol.

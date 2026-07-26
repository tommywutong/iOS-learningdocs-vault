---
title: eccVersion
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.property.json'
content_hash: 'sha256:9221c78288858ef9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)

# eccVersion

<sub>Instance Property</sub>

The error correction version of the Data Matrix code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion { get }
```

## Discussion

The possible error correction version are enumerated in [ECCVersion](eccversion-swift.enum.md). Any symbol with an even number of rows and columns will be ECC 200.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [rowCount](rowcount-swift.property.md) — The number of rows in the Data Matrix code symbol.
- [columnCount](columncount-swift.property.md) — The number of columns in the Data Matrix code symbol.

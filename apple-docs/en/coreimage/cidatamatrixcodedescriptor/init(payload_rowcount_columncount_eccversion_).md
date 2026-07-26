---
title: 'init(payload:rowCount:columnCount:eccVersion:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cidatamatrixcodedescriptor/init(payload:rowcount:columncount:eccversion:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/init(payload:rowcount:columncount:eccversion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor/init%28payload%3Arowcount%3Acolumncount%3Aeccversion%3A%29.json'
content_hash: 'sha256:c8c6729bb19ef044'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)

# init(payload:rowCount:columnCount:eccVersion:)

<sub>Initializer</sub>

Initializes a Data Matrix code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(payload errorCorrectedPayload: Data, rowCount: Int, columnCount: Int, eccVersion: CIDataMatrixCodeDescriptor.ECCVersion)
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the Data Matrix code symbol.

- `rowCount` — The number of rows in the Data Matrix code symbol.

- `columnCount` — The number of columns in the Data Matrix code symbol.

- `eccVersion` — The [ECCVersion](eccversion-swift.enum.md) for the Data Matrix code symbol.

## Return Value

An initialized [CIAztecCodeDescriptor](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

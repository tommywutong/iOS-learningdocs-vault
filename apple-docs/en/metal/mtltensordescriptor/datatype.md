---
title: dataType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor/datatype
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor/datatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor/datatype.json'
content_hash: 'sha256:46a2ba78a5cad2cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorDescriptor](../mtltensordescriptor.md)

# dataType

<sub>Instance Property</sub>

The data format of all elements in the data plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dataType: MTLTensorDataType { get set }
```

## Discussion

The default value of this property is [MTLTensorDataTypeFloat32](../mtltensordatatype/float32.md).

[MTLTensorDataTypeMetalFloat8UE8M0](../mtltensordatatype/metalfloat8ue8m0.md) is not a valid data type for this property.

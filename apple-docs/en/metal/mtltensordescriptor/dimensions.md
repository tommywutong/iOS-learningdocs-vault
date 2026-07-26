---
title: dimensions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor/dimensions
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor/dimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor/dimensions.json'
content_hash: 'sha256:4f7e7c978cfd87eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorDescriptor](../mtltensordescriptor.md)

# dimensions

<sub>Instance Property</sub>

An array of sizes, in elements, one for each dimension of the tensors you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var dimensions: MTLTensorExtents { get set }
```

## Discussion

Every element of the array needs to be greater than `0`.

When [dataType](datatype.md) is [MTLTensorDataTypeInt2](../mtltensordatatype/int2.md), [MTLTensorDataTypeUInt2](../mtltensordatatype/uint2.md), [MTLTensorDataTypeInt4](../mtltensordatatype/int4.md), [MTLTensorDataTypeUInt4](../mtltensordatatype/uint4.md), [MTLTensorDataTypeMetalFloat4E2M1](../mtltensordatatype/metalfloat4e2m1.md), [MTLTensorDataTypeMetalFloat8E4M3](../mtltensordatatype/metalfloat8e4m3.md), [MTLTensorDataTypeMetalFloat8E5M2](../mtltensordatatype/metalfloat8e5m2.md), or [MTLTensorDataTypeMetalFloat8UE8M0](../mtltensordatatype/metalfloat8ue8m0.md):

- The dimension value of the array’s first element needs to be a multiple of 32 elements.
- The extents needs to have at least one dimension.

If the tensor has auxiliary planes, each dimension needs to be evenly divisible by its corresponding block factor.

The default value of this property is a rank one extents with size one.

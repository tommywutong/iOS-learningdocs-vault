---
title: MTLTensorDataType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordatatype
source_url: 'https://developer.apple.com/documentation/metal/mtltensordatatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordatatype.json'
content_hash: 'sha256:8ff22cbf41dd10f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorDataType

<sub>Enumeration</sub>

The possible data types for the elements of a tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTensorDataType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLTensorDataTypeBFloat16](mtltensordatatype/bfloat16.md) — A 16-bit floating point data type with 8 exponent bits, 7 mantissa bits, and 1 sign bit.
- [MTLTensorDataTypeFloat16](mtltensordatatype/float16.md) — A half-precision floating point data type.
- [MTLTensorDataTypeFloat32](mtltensordatatype/float32.md) — A single-precision floating point data type.
- [MTLTensorDataTypeInt16](mtltensordatatype/int16.md) — A 16-bit signed integer data type.
- [MTLTensorDataTypeInt2](mtltensordatatype/int2.md) — A 2-bit signed integer data type. _(beta)_
- [MTLTensorDataTypeInt32](mtltensordatatype/int32.md) — A 32-bit signed integer data type.
- [MTLTensorDataTypeInt4](mtltensordatatype/int4.md) — A 4-bit signed integer data type.
- [MTLTensorDataTypeInt8](mtltensordatatype/int8.md) — An 8-bit signed integer data type.
- [MTLTensorDataTypeMetalFloat4E2M1](mtltensordatatype/metalfloat4e2m1.md) — A 4-bit floating point data type with 2 exponent bits, 1 mantissa bit, and 1 sign bit. _(beta)_
- [MTLTensorDataTypeMetalFloat8E4M3](mtltensordatatype/metalfloat8e4m3.md) — An 8-bit floating point data type with 4 exponent bits, 3 mantissa bits, and 1 sign bit. _(beta)_
- [MTLTensorDataTypeMetalFloat8E5M2](mtltensordatatype/metalfloat8e5m2.md) — An 8-bit floating point data type with 5 exponent bits, 2 mantissa bits, and 1 sign bit. _(beta)_
- [MTLTensorDataTypeMetalFloat8UE8M0](mtltensordatatype/metalfloat8ue8m0.md) — An 8-bit floating point data type with 8 exponent bits, 0 mantissa bits, and no sign bit. _(beta)_
- [MTLTensorDataTypeNone](mtltensordatatype/none.md) — An invalid data type.
- [MTLTensorDataTypeUInt16](mtltensordatatype/uint16.md) — A 16-bit unsigned integer data type.
- [MTLTensorDataTypeUInt2](mtltensordatatype/uint2.md) — A 2-bit unsigned integer data type. _(beta)_
- [MTLTensorDataTypeUInt32](mtltensordatatype/uint32.md) — A 32-bit unsigned integer data type.
- [MTLTensorDataTypeUInt4](mtltensordatatype/uint4.md) — A 4-bit unsigned integer data type.
- [MTLTensorDataTypeUInt8](mtltensordatatype/uint8.md) — An 8-bit unsigned integer data type.

### Initializers

- [init(rawValue:)](<mtltensordatatype/init(rawvalue_).md>)

## See Also

### Tensors

- [MTLTensor](mtltensor.md) — A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [MTLTensorDescriptor](mtltensordescriptor.md) — A configuration type for creating new tensor instances.
- [MTLTensorExtents](mtltensorextents.md) — An integer array that holds per-dimension values such as tensor sizes, strides, or block factors
- [MTLTensorReferenceType](mtltensorreferencetype.md) — An object that represents a tensor in the shading language in a struct or array.
- [MTLTensorUsage](mtltensorusage.md) — The contexts in which you can use a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTLTensorBinding](mtltensorbinding.md) — An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [MTLTensorError](mtltensorerror-swift.struct.md)
- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md)

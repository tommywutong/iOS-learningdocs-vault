---
title: MTLVertexFormat
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexformat
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexformat.json'
content_hash: 'sha256:bf6737cd19bcf9ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexFormat

<sub>Enumeration</sub>

The vertex data format options for render pipelines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLVertexFormat
```

## Overview

Set the [format](mtlvertexattributedescriptor/format.md) property of [MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md) to one of these format values. The format configures how Metal interprets the vertex data in memory for the corresponding argument in your vertex shader. Choose a format that matches the type and component count the shader expects.

### Normalized integer formats

Normalized signed integer formats have `Normalized` in the name and signed types like [MTLVertexFormatChar](mtlvertexformat/char.md) or [MTLVertexFormatShort](mtlvertexformat/short.md). For these formats, values in the range `[-1.0, 1.0]` map to `[MIN_INT, MAX_INT]`, where `MIN_INT` is the most negative integer and `MAX_INT` is the most positive integer for the number of bits in the storage size. Positive values and zero distribute uniformly in the range `[0.0, 1.0]`, and negative integer values greater than `(MIN_INT + 1)` distribute uniformly in the range `(-1.0, 0.0)`.

> [!important] Important
> For normalized signed integer formats, the values `MIN_INT` and `(MIN_INT + 1)` both map to `-1.0`.

Normalized unsigned integer formats have `Normalized` in the name and unsigned types like [MTLVertexFormatUChar](mtlvertexformat/uchar.md) or [MTLVertexFormatUShort](mtlvertexformat/ushort.md). For these formats, values in the range `[0.0, 1.0]` map to `[0, MAX_UINT]`, where `MAX_UINT` is the largest unsigned integer for the number of bits in the storage size.

Metal stores data in little-endian byte order, with the least-significant byte at the lowest memory address. Formats with multibyte components also store each component in little-endian byte order.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### 32-bit floating-point formats

- [MTLVertexFormatFloat](mtlvertexformat/float.md) — A 32-bit floating-point value.
- [MTLVertexFormatFloat2](mtlvertexformat/float2.md) — A two-component vector with 32-bit floating-point values.
- [MTLVertexFormatFloat3](mtlvertexformat/float3.md) — A three-component vector with 32-bit floating-point values.
- [MTLVertexFormatFloat4](mtlvertexformat/float4.md) — A four-component vector with 32-bit floating-point values.
- [MTLVertexFormatFloatRG11B10](mtlvertexformat/floatrg11b10.md) — A three-component vector with 11-bit floating-point values for red and green, and a 10-bit value for blue.
- [MTLVertexFormatFloatRGB9E5](mtlvertexformat/floatrgb9e5.md) — A three-component vector with 9-bit floating-point values for red, green, and blue, and a 5-bit shared exponent.

### 32-bit integer formats

- [MTLVertexFormatInt](mtlvertexformat/int.md) — A 32-bit, signed integer value.
- [MTLVertexFormatInt2](mtlvertexformat/int2.md) — A two-component vector with 32-bit, signed integer values.
- [MTLVertexFormatInt3](mtlvertexformat/int3.md) — A three-component vector with 32-bit, signed integer values.
- [MTLVertexFormatInt4](mtlvertexformat/int4.md) — A four-component vector with 32-bit, signed integer values.
- [MTLVertexFormatUInt](mtlvertexformat/uint.md) — A 32-bit, unsigned integer value.
- [MTLVertexFormatUInt2](mtlvertexformat/uint2.md) — A two-component vector with 32-bit, unsigned integer values.
- [MTLVertexFormatUInt3](mtlvertexformat/uint3.md) — A three-component vector with 32-bit, unsigned integer values.
- [MTLVertexFormatUInt4](mtlvertexformat/uint4.md) — A four-component vector with 32-bit, unsigned integer values.

### 32-bit normalized integer formats

- [MTLVertexFormatInt1010102Normalized](mtlvertexformat/int1010102normalized.md) — A four-component vector with 10-bit, normalized, signed integer values for red, green, and blue, and a 2-bit value for alpha.
- [MTLVertexFormatUInt1010102Normalized](mtlvertexformat/uint1010102normalized.md) — A four-component vector with 10-bit, normalized, unsigned integer values for red, green, and blue, and a 2-bit value for alpha.
- [MTLVertexFormatUChar4Normalized_BGRA](mtlvertexformat/uchar4normalized_bgra.md) — A four-component vector with 8-bit, normalized, unsigned integer values for blue, green, red, and alpha.

### 16-bit floating-point formats

- [MTLVertexFormatHalf](mtlvertexformat/half.md) — A 16-bit floating-point value.
- [MTLVertexFormatHalf2](mtlvertexformat/half2.md) — A two-component vector with 16-bit floating-point values.
- [MTLVertexFormatHalf3](mtlvertexformat/half3.md) — A three-component vector with 16-bit floating-point values.
- [MTLVertexFormatHalf4](mtlvertexformat/half4.md) — A four-component vector with 16-bit floating-point values.

### 16-bit integer formats

- [MTLVertexFormatShort](mtlvertexformat/short.md) — A 16-bit, signed integer value.
- [MTLVertexFormatShort2](mtlvertexformat/short2.md) — A two-component vector with 16-bit, signed integer values.
- [MTLVertexFormatShort3](mtlvertexformat/short3.md) — A three-component vector with 16-bit, signed integer values.
- [MTLVertexFormatShort4](mtlvertexformat/short4.md) — A four-component vector with 16-bit, signed integer values.
- [MTLVertexFormatUShort](mtlvertexformat/ushort.md) — A 16-bit, unsigned integer value.
- [MTLVertexFormatUShort2](mtlvertexformat/ushort2.md) — A two-component vector with 16-bit, unsigned integer values.
- [MTLVertexFormatUShort3](mtlvertexformat/ushort3.md) — A three-component vector with 16-bit, unsigned integer values.
- [MTLVertexFormatUShort4](mtlvertexformat/ushort4.md) — A four-component vector with 16-bit, unsigned integer values.

### 16-bit normalized integer formats

- [MTLVertexFormatShortNormalized](mtlvertexformat/shortnormalized.md) — A 16-bit, normalized, signed integer value.
- [MTLVertexFormatShort2Normalized](mtlvertexformat/short2normalized.md) — A two-component vector with 16-bit, normalized, signed integer values.
- [MTLVertexFormatShort3Normalized](mtlvertexformat/short3normalized.md) — A three-component vector with 16-bit, normalized, signed integer values.
- [MTLVertexFormatShort4Normalized](mtlvertexformat/short4normalized.md) — A four-component vector with 16-bit, normalized, signed integer values.
- [MTLVertexFormatUShortNormalized](mtlvertexformat/ushortnormalized.md) — A 16-bit, normalized, unsigned integer value.
- [MTLVertexFormatUShort2Normalized](mtlvertexformat/ushort2normalized.md) — A two-component vector with 16-bit, normalized, unsigned integer values.
- [MTLVertexFormatUShort3Normalized](mtlvertexformat/ushort3normalized.md) — A three-component vector with 16-bit, normalized, unsigned integer values.
- [MTLVertexFormatUShort4Normalized](mtlvertexformat/ushort4normalized.md) — A four-component vector with 16-bit, normalized, unsigned integer values.

### 8-bit integer formats

- [MTLVertexFormatChar](mtlvertexformat/char.md) — An 8-bit, signed integer value.
- [MTLVertexFormatChar2](mtlvertexformat/char2.md) — A two-component vector with 8-bit, signed integer values.
- [MTLVertexFormatChar3](mtlvertexformat/char3.md) — A three-component vector with 8-bit, signed integer values.
- [MTLVertexFormatChar4](mtlvertexformat/char4.md) — A four-component vector with 8-bit, signed integer values.
- [MTLVertexFormatUChar](mtlvertexformat/uchar.md) — An 8-bit, unsigned integer value.
- [MTLVertexFormatUChar2](mtlvertexformat/uchar2.md) — A two-component vector with 8-bit, unsigned integer values.
- [MTLVertexFormatUChar3](mtlvertexformat/uchar3.md) — A three-component vector with 8-bit, unsigned integer values.
- [MTLVertexFormatUChar4](mtlvertexformat/uchar4.md) — A four-component vector with 8-bit, unsigned integer values.

### 8-bit normalized integer formats

- [MTLVertexFormatCharNormalized](mtlvertexformat/charnormalized.md) — An 8-bit, normalized, signed integer value.
- [MTLVertexFormatChar2Normalized](mtlvertexformat/char2normalized.md) — A two-component vector with 8-bit, normalized, signed integer values.
- [MTLVertexFormatChar3Normalized](mtlvertexformat/char3normalized.md) — A three-component vector with 8-bit, normalized, signed integer values.
- [MTLVertexFormatChar4Normalized](mtlvertexformat/char4normalized.md) — A four-component vector with 8-bit, normalized, signed integer values.
- [MTLVertexFormatUCharNormalized](mtlvertexformat/ucharnormalized.md) — An 8-bit, normalized, unsigned integer value.
- [MTLVertexFormatUChar2Normalized](mtlvertexformat/uchar2normalized.md) — A two-component vector with 8-bit, normalized, unsigned integer values.
- [MTLVertexFormatUChar3Normalized](mtlvertexformat/uchar3normalized.md) — A three-component vector with 8-bit, normalized, unsigned integer values.
- [MTLVertexFormatUChar4Normalized](mtlvertexformat/uchar4normalized.md) — A four-component vector with 8-bit, normalized, unsigned integer values.

### Sentinel values

- [MTLVertexFormatInvalid](mtlvertexformat/invalid.md) — A sentinel value that represents an empty set of vertex format options.

### Swift support

- [init(rawValue:)](<mtlvertexformat/init(rawvalue_).md>) — Creates a vertex format from a raw integer value.

## See Also

### Organizing the vertex attribute

- [format](mtlvertexattributedescriptor/format.md) — The format of the vertex attribute.
- [offset](mtlvertexattributedescriptor/offset.md) — The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [bufferIndex](mtlvertexattributedescriptor/bufferindex.md) — The index in the argument table for the associated vertex buffer.

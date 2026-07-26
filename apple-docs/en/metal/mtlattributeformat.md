---
title: MTLAttributeFormat
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattributeformat
source_url: 'https://developer.apple.com/documentation/metal/mtlattributeformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributeformat.json'
content_hash: 'sha256:169d0492f3f27961'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAttributeFormat

<sub>Enumeration</sub>

The data format options for acceleration structures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLAttributeFormat
```

## Overview

All formats use little-endian byte order, which stores the least significant byte first. For GPU compute functions that manipulate data that other parts of your app consume, check that the data it exposes to the GPU matches the byte and bit alignments of the source format.

In a GPU compute function’s attributes, you can use a type that’s different from the original source data if it has the same number of bits. For example, a GPU function can interpret a 128-bit little-endian integer as a four-component vector of unsigned 32-bit integers ([MTLAttributeFormatUInt4](mtlattributeformat/uint4.md)).

> [!tip] Tip
> Avoid visual corruption when manipulating pixel data in a GPU compute function for a subsequent stage by using an exact match for the underlying pixel data.

### Normalized integer formats

Normalized signed integer formats have `Normalized` in the name and signed types like [MTLAttributeFormatChar](mtlattributeformat/char.md) or [MTLAttributeFormatShort](mtlattributeformat/short.md). For these formats, values in the range `[-1.0, 1.0]` map to `[MIN_INT, MAX_INT]`, where `MIN_INT` is the most negative integer and `MAX_INT` is the most positive integer for the number of bits in the storage size. Positive values and zero distribute uniformly in the range `[0.0, 1.0]`, and negative integer values greater than `(MIN_INT + 1)` distribute uniformly in the range `(-1.0, 0.0)`.

> [!important] Important
> For normalized signed integer formats, the values `MIN_INT` and `(MIN_INT + 1)` both map to `-1.0`.

Normalized unsigned integer formats have `Normalized` in the name and unsigned types like [MTLAttributeFormatUChar](mtlattributeformat/uchar.md) or [MTLAttributeFormatUShort](mtlattributeformat/ushort.md). For these formats, values in the range `[0.0, 1.0]` map to `[0, MAX_UINT]`, where `MAX_UINT` is the largest unsigned integer for the number of bits in the storage size.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### 32-bit floating-point formats

- [MTLAttributeFormatFloat](mtlattributeformat/float.md) — A 32-bit floating-point value.
- [MTLAttributeFormatFloat2](mtlattributeformat/float2.md) — A two-component vector with 32-bit floating-point values.
- [MTLAttributeFormatFloat3](mtlattributeformat/float3.md) — A three-component vector with 32-bit floating-point values.
- [MTLAttributeFormatFloat4](mtlattributeformat/float4.md) — A four-component vector with 32-bit floating-point values.
- [MTLAttributeFormatFloatRG11B10](mtlattributeformat/floatrg11b10.md) — One packed 32-bit value representing pixel data containing 11-bit float red and green channels, and a 10-bit float blue channel.
- [MTLAttributeFormatFloatRGB9E5](mtlattributeformat/floatrgb9e5.md) — One packed 32-bit value representing pixel data containing 9-bit float red, green, and blue channels, and a 5-bit float shared exponent channel.

### 32-bit integer formats

- [MTLAttributeFormatInt](mtlattributeformat/int.md) — A 32-bit, signed integer value.
- [MTLAttributeFormatInt2](mtlattributeformat/int2.md) — A two-component vector with 32-bit, signed integer values.
- [MTLAttributeFormatInt3](mtlattributeformat/int3.md) — A three-component vector with 32-bit, signed integer values.
- [MTLAttributeFormatInt4](mtlattributeformat/int4.md) — A four-component vector with 32-bit, signed integer values.
- [MTLAttributeFormatUInt](mtlattributeformat/uint.md) — A 32-bit, unsigned integer value.
- [MTLAttributeFormatUInt2](mtlattributeformat/uint2.md) — A two-component vector with 32-bit, unsigned integer values.
- [MTLAttributeFormatUInt3](mtlattributeformat/uint3.md) — A three-component vector with 32-bit, unsigned integer values.
- [MTLAttributeFormatUInt4](mtlattributeformat/uint4.md) — A four-component vector with 32-bit, unsigned integer values.

### 32-bit normalized integer formats

- [MTLAttributeFormatInt1010102Normalized](mtlattributeformat/int1010102normalized.md) — One packed 32-bit value with four normalized signed two’s complement integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
- [MTLAttributeFormatUInt1010102Normalized](mtlattributeformat/uint1010102normalized.md) — One packed 32-bit value with four normalized unsigned integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
- [MTLAttributeFormatUChar4Normalized_BGRA](mtlattributeformat/uchar4normalized_bgra.md) — Four unsigned normalized 8-bit values, arranged as blue, green, red, and alpha components.

### 16-bit floating-point formats

- [MTLAttributeFormatHalf](mtlattributeformat/half.md) — A 16-bit floating-point value.
- [MTLAttributeFormatHalf2](mtlattributeformat/half2.md) — A two-component vector with 16-bit floating-point values.
- [MTLAttributeFormatHalf3](mtlattributeformat/half3.md) — A three-component vector with 16-bit floating-point values.
- [MTLAttributeFormatHalf4](mtlattributeformat/half4.md) — A four-component vector with 16-bit floating-point values.

### 16-bit integer formats

- [MTLAttributeFormatShort](mtlattributeformat/short.md) — A 16-bit, signed integer value.
- [MTLAttributeFormatShort2](mtlattributeformat/short2.md) — A two-component vector with 16-bit, signed integer values.
- [MTLAttributeFormatShort3](mtlattributeformat/short3.md) — A three-component vector with 16-bit, signed integer values.
- [MTLAttributeFormatShort4](mtlattributeformat/short4.md) — A four-component vector with 16-bit, signed integer values.
- [MTLAttributeFormatUShort](mtlattributeformat/ushort.md) — A 16-bit, unsigned integer value.
- [MTLAttributeFormatUShort2](mtlattributeformat/ushort2.md) — A two-component vector with 16-bit, unsigned integer values.
- [MTLAttributeFormatUShort3](mtlattributeformat/ushort3.md) — A three-component vector with 16-bit, unsigned integer values.
- [MTLAttributeFormatUShort4](mtlattributeformat/ushort4.md) — A four-component vector with 16-bit, unsigned integer values.

### 16-bit normalized integer formats

- [MTLAttributeFormatShortNormalized](mtlattributeformat/shortnormalized.md) — A 16-bit, normalized, signed integer value.
- [MTLAttributeFormatShort2Normalized](mtlattributeformat/short2normalized.md) — A two-component vector with 16-bit, normalized, signed integer values.
- [MTLAttributeFormatShort3Normalized](mtlattributeformat/short3normalized.md) — A three-component vector with 16-bit, normalized, signed integer values.
- [MTLAttributeFormatShort4Normalized](mtlattributeformat/short4normalized.md) — A four-component vector with 16-bit, normalized, signed integer values.
- [MTLAttributeFormatUShortNormalized](mtlattributeformat/ushortnormalized.md) — A 16-bit, normalized, unsigned integer value.
- [MTLAttributeFormatUShort2Normalized](mtlattributeformat/ushort2normalized.md) — Two unsigned normalized 16-bit values
- [MTLAttributeFormatUShort3Normalized](mtlattributeformat/ushort3normalized.md) — A three-component vector with 16-bit, normalized, unsigned integer values.
- [MTLAttributeFormatUShort4Normalized](mtlattributeformat/ushort4normalized.md) — A four-component vector with 16-bit, normalized, unsigned integer values.

### 8-bit integer formats

- [MTLAttributeFormatChar](mtlattributeformat/char.md) — An 8-bit, signed integer value.
- [MTLAttributeFormatChar2](mtlattributeformat/char2.md) — A two-component vector with 8-bit, signed integer values.
- [MTLAttributeFormatChar3](mtlattributeformat/char3.md) — A three-component vector with 8-bit, signed integer values.
- [MTLAttributeFormatChar4](mtlattributeformat/char4.md) — A four-component vector with 8-bit, signed integer values.
- [MTLAttributeFormatUChar](mtlattributeformat/uchar.md) — An 8-bit, unsigned integer value.
- [MTLAttributeFormatUChar2](mtlattributeformat/uchar2.md) — A two-component vector with 8-bit, unsigned integer values.
- [MTLAttributeFormatUChar3](mtlattributeformat/uchar3.md) — A three-component vector with 8-bit, unsigned integer values.
- [MTLAttributeFormatUChar4](mtlattributeformat/uchar4.md) — A four-component vector with 8-bit, unsigned integer values.

### 8-bit normalized integer formats

- [MTLAttributeFormatCharNormalized](mtlattributeformat/charnormalized.md) — An 8-bit, normalized, signed integer value.
- [MTLAttributeFormatChar2Normalized](mtlattributeformat/char2normalized.md) — A two-component vector with 8-bit, normalized, signed integer values.
- [MTLAttributeFormatChar3Normalized](mtlattributeformat/char3normalized.md) — A three-component vector with 8-bit, normalized, signed integer values.
- [MTLAttributeFormatChar4Normalized](mtlattributeformat/char4normalized.md) — A four-component vector with 8-bit, normalized, signed integer values.
- [MTLAttributeFormatUCharNormalized](mtlattributeformat/ucharnormalized.md) — An 8-bit, normalized, unsigned integer value.
- [MTLAttributeFormatUChar2Normalized](mtlattributeformat/uchar2normalized.md) — A two-component vector with 8-bit, normalized, unsigned integer values.
- [MTLAttributeFormatUChar3Normalized](mtlattributeformat/uchar3normalized.md) — A three-component vector with 8-bit, normalized, unsigned integer values.
- [MTLAttributeFormatUChar4Normalized](mtlattributeformat/uchar4normalized.md) — A four-component vector with 8-bit, normalized, unsigned integer values.

### Sentinel values

- [MTLAttributeFormatInvalid](mtlattributeformat/invalid.md) — A sentinel value that represents an invalid attribute format.

### Swift support

- [init(rawValue:)](<mtlattributeformat/init(rawvalue_).md>)

## See Also

### Defining attribute location

- [bufferIndex](mtlattributedescriptor/bufferindex.md) — The index in the buffer argument table for the buffer that contains the data for this attribute.
- [offset](mtlattributedescriptor/offset.md) — The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.
- [format](mtlattributedescriptor/format.md) — The format of the attribute’s data.

---
title: 'setBuffer(_:offset:for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtltensorbufferattachments/setbuffer(_:offset:for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorbufferattachments/setbuffer(_:offset:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorbufferattachments/setbuffer%28_%3Aoffset%3Afor%3A%29.json'
content_hash: 'sha256:cbf6137c1efa12a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorBufferAttachments](../mtltensorbufferattachments.md)

# setBuffer(_:offset:for:)

<sub>Instance Method</sub>

Sets the buffer and byte offset to use as backing storage for the given plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBuffer(_ buffer: any MTLBuffer, offset: Int, for plane: MTLTensorPlaneType)
```

## Parameters

- `buffer` — The buffer to back the plane.

- `offset` — The byte offset into the buffer.

- `plane` — The plane type to associate the buffer with.

## Discussion

The offset needs to be aligned to 128 bytes if the plane uses [MTLTensorDataTypeInt2](../mtltensordatatype/int2.md), [MTLTensorDataTypeUInt2](../mtltensordatatype/uint2.md), [MTLTensorDataTypeInt4](../mtltensordatatype/int4.md), [MTLTensorDataTypeUInt4](../mtltensordatatype/uint4.md), [MTLTensorDataTypeMetalFloat4E2M1](../mtltensordatatype/metalfloat4e2m1.md), [MTLTensorDataTypeMetalFloat8E4M3](../mtltensordatatype/metalfloat8e4m3.md), [MTLTensorDataTypeMetalFloat8E5M2](../mtltensordatatype/metalfloat8e5m2.md), or [MTLTensorDataTypeMetalFloat8UE8M0](../mtltensordatatype/metalfloat8ue8m0.md), otherwise it needs to be aligned to the size of the plane’s data type in bytes.

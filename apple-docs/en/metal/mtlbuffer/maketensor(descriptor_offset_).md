---
title: 'makeTensor(descriptor:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbuffer/maketensor(descriptor:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/maketensor(descriptor:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/maketensor%28descriptor%3Aoffset%3A%29.json'
content_hash: 'sha256:414a08f9399c42ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# makeTensor(descriptor:offset:)

<sub>Instance Method</sub>

Creates a single-plane tensor with the specified descriptor that shares storage with this buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTensor(descriptor: MTLTensorDescriptor, offset: Int) throws -> any MTLTensor
```

## Parameters

- `descriptor` — The tensor descriptor configuring the data plane.

- `offset` — The byte offset into the buffer where tensor data begins.

## Return Value

A tensor, or `nil` if validation fails.

## Discussion

This method validates the constraints documented on [MTLTensorDescriptor](../mtltensordescriptor.md), and additionally requires:

- `offset` is 0 when [usage](../mtltensordescriptor/usage.md) contains [MTLTensorUsageMachineLearning](../mtltensorusage/machinelearning.md).
- `offset` is aligned to 128 bytes if the data plane uses a format [MTLTensorDataType](../mtltensordatatype.md).
- `offset` is aligned to the size of the data type in bytes otherwise.

This method doesn’t create tensors that contain auxiliary planes. Use [- newTensorWithDescriptor:attachments:error:](<../mtldevice/maketensor(descriptor_attachments_).md>) instead to create a multi-plane tensor with per-plane buffer backing storage.

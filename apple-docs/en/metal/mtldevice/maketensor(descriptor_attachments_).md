---
title: 'makeTensor(descriptor:attachments:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtldevice/maketensor(descriptor:attachments:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maketensor(descriptor:attachments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maketensor%28descriptor%3Aattachments%3A%29.json'
content_hash: 'sha256:7b728e5123f5ff3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeTensor(descriptor:attachments:)

<sub>Instance Method</sub>

Creates a tensor with the specified descriptor and per-plane buffer backing storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTensor(descriptor: MTLTensorDescriptor, attachments: MTLTensorBufferAttachments) throws -> any MTLTensor
```

## Parameters

- `descriptor` — The tensor descriptor configuring the data plane and auxiliary planes.

- `attachments` — The per-plane buffer backing storage. Must not be `nil`.

## Return Value

A tensor, or `nil` if validation fails.

## Discussion

This method validates the constraints documented on [MTLTensorDescriptor](../mtltensordescriptor.md) and [MTLTensorBufferAttachments](../mtltensorbufferattachments.md), and additionally requires that every plane configured in `descriptor` (data plane and all auxiliary planes) has a corresponding entry in `attachments`.

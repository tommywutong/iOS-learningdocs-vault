---
title: 'makeTensor(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/maketensor(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maketensor(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maketensor%28descriptor%3A%29.json'
content_hash: 'sha256:f50c6b8d171fa6e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeTensor(descriptor:)

<sub>Instance Method</sub>

Creates a tensor with the specified descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTensor(descriptor: MTLTensorDescriptor) throws -> any MTLTensor
```

## Parameters

- `descriptor` — The tensor descriptor configuring the data plane and auxiliary planes.

## Return Value

A tensor, or `nil` if validation fails.

## Discussion

This method validates the constraints documented on [MTLTensorDescriptor](../mtltensordescriptor.md).

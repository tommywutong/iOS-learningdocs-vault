---
title: 'tensorSizeAndAlign(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/tensorsizeandalign(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/tensorsizeandalign(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/tensorsizeandalign%28descriptor%3A%29.json'
content_hash: 'sha256:7626339ced05a7c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# tensorSizeAndAlign(descriptor:)

<sub>Instance Method</sub>

Determines the size and alignment required to hold the data of a tensor you create with a descriptor in a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func tensorSizeAndAlign(descriptor: MTLTensorDescriptor) -> MTLSizeAndAlign
```

## Parameters

- `descriptor` — A description of the properties for the new tensor.

## Return Value

The size and alignment required to hold the data of a tensor you create with `descriptor` in a buffer.

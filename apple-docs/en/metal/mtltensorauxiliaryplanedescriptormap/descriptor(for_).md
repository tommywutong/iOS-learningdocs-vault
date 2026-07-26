---
title: 'descriptor(for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtltensorauxiliaryplanedescriptormap/descriptor(for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap/descriptor(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorauxiliaryplanedescriptormap/descriptor%28for%3A%29.json'
content_hash: 'sha256:b653f256b195949f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorAuxiliaryPlaneDescriptorMap](../mtltensorauxiliaryplanedescriptormap.md)

# descriptor(for:)

<sub>Instance Method</sub>

Returns the auxiliary plane descriptor for the given plane type, or `nil` if none has been set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func descriptor(for plane: MTLTensorPlaneType) -> MTLTensorAuxiliaryPlaneDescriptor?
```

## Parameters

- `plane` — The plane type to look up.

## Return Value

The descriptor for the given plane type, or `nil`.

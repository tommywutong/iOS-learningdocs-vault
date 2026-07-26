---
title: storageMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor/storagemode
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor/storagemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor/storagemode.json'
content_hash: 'sha256:731bca78a21f8453'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorDescriptor](../mtltensordescriptor.md)

# storageMode

<sub>Instance Property</sub>

A value that configures the memory location and access permissions of tensors you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var storageMode: MTLStorageMode { get set }
```

## Discussion

The default value of this property is [MTLStorageModeShared](../mtlstoragemode/shared.md).

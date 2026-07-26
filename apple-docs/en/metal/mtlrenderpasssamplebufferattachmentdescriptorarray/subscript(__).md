---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:3d007296301a7fc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassSampleBufferAttachmentDescriptorArray](../mtlrenderpasssamplebufferattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the descriptor object for the specified sample buffer attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTLRenderPassSampleBufferAttachmentDescriptor! { get set }
```

## Parameters

- `attachmentIndex` — An index for the object to fetch.

## Return Value

The [MTLRenderPassSampleBufferAttachmentDescriptor](../mtlrenderpasssamplebufferattachmentdescriptor.md) at the specified index.

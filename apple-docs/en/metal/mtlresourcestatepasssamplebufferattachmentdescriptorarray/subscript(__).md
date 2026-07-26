---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:21b47bdc8a6d5a58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStatePassSampleBufferAttachmentDescriptorArray](../mtlresourcestatepasssamplebufferattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the descriptor object for the specified sample buffer attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTLResourceStatePassSampleBufferAttachmentDescriptor! { get set }
```

## Parameters

- `attachmentIndex` — An index for the object to fetch.

## Return Value

The requested [MTLResourceStatePassSampleBufferAttachmentDescriptor](../mtlresourcestatepasssamplebufferattachmentdescriptor.md) object.

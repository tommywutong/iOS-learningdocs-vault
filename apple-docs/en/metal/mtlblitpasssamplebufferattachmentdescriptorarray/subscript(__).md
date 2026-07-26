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
doc_path: '/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:7a17f6599af52e58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitPassSampleBufferAttachmentDescriptorArray](../mtlblitpasssamplebufferattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses one of the array’s blit pass sample buffer attachment descriptor instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTLBlitPassSampleBufferAttachmentDescriptor! { get set }
```

## Parameters

- `attachmentIndex` — An index of one of the array’s [MTLBlitPassSampleBufferAttachmentDescriptor](../mtlblitpasssamplebufferattachmentdescriptor.md) instances.

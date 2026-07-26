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
doc_path: '/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:c47515dd4832febc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePassSampleBufferAttachmentDescriptorArray](../mtlcomputepasssamplebufferattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the descriptor object for the specified sample buffer attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTLComputePassSampleBufferAttachmentDescriptor! { get set }
```

## Parameters

- `attachmentIndex` — An index for the sample buffer attachment to fetch.

## Return Value

The requested  [MTLComputePassSampleBufferAttachmentDescriptor](../mtlcomputepasssamplebufferattachmentdescriptor.md) object.

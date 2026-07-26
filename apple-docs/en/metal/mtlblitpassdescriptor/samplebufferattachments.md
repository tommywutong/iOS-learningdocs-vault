---
title: sampleBufferAttachments
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitpassdescriptor/samplebufferattachments
source_url: 'https://developer.apple.com/documentation/metal/mtlblitpassdescriptor/samplebufferattachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitpassdescriptor/samplebufferattachments.json'
content_hash: 'sha256:35d9e07a5971389b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitPassDescriptor](../mtlblitpassdescriptor.md)

# sampleBufferAttachments

<sub>Instance Property</sub>

An array of counter sample buffer attachments that you configure for a blit pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBufferAttachments: MTLBlitPassSampleBufferAttachmentDescriptorArray { get }
```

## Discussion

See [Sampling GPU data into counter sample buffers](../sampling-gpu-data-into-counter-sample-buffers.md) for more context about configuring this property. That article is one of a series of articles in [GPU counters and counter sample buffers](../gpu-counters-and-counter-sample-buffers.md).

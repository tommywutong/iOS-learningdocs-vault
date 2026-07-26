---
title: sampleBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurepasssamplebufferattachmentdescriptor/samplebuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurepasssamplebufferattachmentdescriptor/samplebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurepasssamplebufferattachmentdescriptor/samplebuffer.json'
content_hash: 'sha256:1aa95a20abd82c1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructurePassSampleBufferAttachmentDescriptor](../mtlaccelerationstructurepasssamplebufferattachmentdescriptor.md)

# sampleBuffer

<sub>Instance Property</sub>

A specialized memory buffer that the GPU uses to store its counter data during the acceleration structure pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBuffer: (any MTLCounterSampleBuffer)? { get set }
```

## Discussion

The property defaults to `nil`, which means the GPU doesn’t save any GPU counter information during the acceleration structure pass. See [Creating a counter sample buffer to store a GPU’s counter data during a pass](../creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) and [Sampling GPU data into counter sample buffers](../sampling-gpu-data-into-counter-sample-buffers.md) for more information.

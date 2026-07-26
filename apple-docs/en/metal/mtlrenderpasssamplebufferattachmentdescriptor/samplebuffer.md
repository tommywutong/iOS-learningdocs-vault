---
title: sampleBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/samplebuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/samplebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/samplebuffer.json'
content_hash: 'sha256:0f2b0ca717494c21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassSampleBufferAttachmentDescriptor](../mtlrenderpasssamplebufferattachmentdescriptor.md)

# sampleBuffer

<sub>Instance Property</sub>

A specialized memory buffer that the GPU uses to store its counter data during the render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBuffer: (any MTLCounterSampleBuffer)? { get set }
```

## Discussion

The property defaults to `nil`, which means the GPU doesn’t save any GPU counter information during the render pass. For more information, see [Creating a counter sample buffer to store a GPU’s counter data during a pass](../creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) and [Sampling GPU data into counter sample buffers](../sampling-gpu-data-into-counter-sample-buffers.md).

## See Also

### Configuring the sample buffer attachment

- [startOfVertexSampleIndex](startofvertexsampleindex.md) — The index the Metal device object should use to store GPU counters when starting the render pass’s vertex stage.
- [endOfVertexSampleIndex](endofvertexsampleindex.md) — The index the Metal device object should use to store GPU counters when ending the render pass’s vertex stage.
- [startOfFragmentSampleIndex](startoffragmentsampleindex.md) — The index the Metal device object should use to store GPU counters when starting the render pass’s fragment stage.
- [endOfFragmentSampleIndex](endoffragmentsampleindex.md) — The index the Metal device object should use to store GPU counters when ending the render pass’s fragment stage.

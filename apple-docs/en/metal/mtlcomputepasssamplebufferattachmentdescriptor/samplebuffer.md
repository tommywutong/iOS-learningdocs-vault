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
doc_path: /documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer.json'
content_hash: 'sha256:00a609b1e0450dc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePassSampleBufferAttachmentDescriptor](../mtlcomputepasssamplebufferattachmentdescriptor.md)

# sampleBuffer

<sub>Instance Property</sub>

A specialized memory buffer that the GPU uses to store its counter data during a compute pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBuffer: (any MTLCounterSampleBuffer)? { get set }
```

## Discussion

The property defaults to `nil`, which means the GPU doesn’t save any GPU counter information during the compute pass. For more information, see [Creating a counter sample buffer to store a GPU’s counter data during a pass](../creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) and [Sampling GPU data into counter sample buffers](../sampling-gpu-data-into-counter-sample-buffers.md).

## See Also

### Configuring the sample buffer attachment

- [startOfEncoderSampleIndex](startofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the start of a compute pass.
- [endOfEncoderSampleIndex](endofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the end of a compute pass.

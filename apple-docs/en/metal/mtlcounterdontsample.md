---
title: MTLCounterDontSample
framework: Metal
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterdontsample
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterdontsample'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterdontsample.json'
content_hash: 'sha256:7f88f55ee1b8c0fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterDontSample

<sub>Global Variable</sub>

A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var MTLCounterDontSample: Int { get }
```

## Discussion

You can skip sampling at specific stages by assigning this sentinel value to the following properties instead of an offset to a counter sample buffer:

| Types | Properties |
|---|---|
| [MTLRenderPassSampleBufferAttachmentDescriptor](mtlrenderpasssamplebufferattachmentdescriptor.md) | [startOfVertexSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfVertexSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [startOfFragmentSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfFragmentSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex.md) |
| [MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md) | [startOfEncoderSampleIndex](mtlcomputepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [MTLBlitPassSampleBufferAttachmentDescriptor](mtlblitpasssamplebufferattachmentdescriptor.md) | [startOfEncoderSampleIndex](mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [MTLResourceStatePassSampleBufferAttachmentDescriptor](mtlresourcestatepasssamplebufferattachmentdescriptor.md) | [startOfEncoderSampleIndex](mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [MTLAccelerationStructurePassSampleBufferAttachmentDescriptor](mtlaccelerationstructurepasssamplebufferattachmentdescriptor.md) | [startOfEncoderSampleIndex](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |

## See Also

### Counter sample buffers

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) — Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md) — A group of properties that configures the counter sample buffers you create with it.
- [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) — A specialized memory buffer that stores a GPU’s counter set data.
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) — Retrieve a GPU’s counter data at a time the GPU supports.

---
title: startOfVertexSampleIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.json'
content_hash: 'sha256:2e6d6114908dc75e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassSampleBufferAttachmentDescriptor](../mtlrenderpasssamplebufferattachmentdescriptor.md)

# startOfVertexSampleIndex

<sub>Instance Property</sub>

The index the Metal device object should use to store GPU counters when starting the render pass’s vertex stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var startOfVertexSampleIndex: Int { get set }
```

## Discussion

Specify [MTLCounterDontSample](../mtlcounterdontsample.md) if you don’t want to sample GPU counters at the start of the vertex stage. Otherwise, specify an index within the sample buffer where you want the GPU to write the sample data.

On devices that don’t support [MTLCounterSamplingPointAtStageBoundary](../mtlcountersamplingpoint/atstageboundary.md) you need to set the value to [MTLCounterDontSample](../mtlcounterdontsample.md).

## See Also

### Configuring the sample buffer attachment

- [sampleBuffer](samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during the render pass.
- [endOfVertexSampleIndex](endofvertexsampleindex.md) — The index the Metal device object should use to store GPU counters when ending the render pass’s vertex stage.
- [startOfFragmentSampleIndex](startoffragmentsampleindex.md) — The index the Metal device object should use to store GPU counters when starting the render pass’s fragment stage.
- [endOfFragmentSampleIndex](endoffragmentsampleindex.md) — The index the Metal device object should use to store GPU counters when ending the render pass’s fragment stage.

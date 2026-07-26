---
title: endOfEncoderSampleIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.json'
content_hash: 'sha256:1438223d11ad6d44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePassSampleBufferAttachmentDescriptor](../mtlcomputepasssamplebufferattachmentdescriptor.md)

# endOfEncoderSampleIndex

<sub>Instance Property</sub>

An index within a counter sample buffer that tells the GPU where to store counter data from the end of a compute pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var endOfEncoderSampleIndex: Int { get set }
```

## Discussion

This property indicates where the GPU stores the counter data within an [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md) instance that it samples at the end of a compute pass.

You can tell the GPU to skip sampling at the end of the compute pass by assigning [MTLCounterDontSample](../mtlcounterdontsample.md) to this property.

> [!important] Important
> For [MTLDevice](../mtldevice.md) instances that don’t support [MTLCounterSamplingPointAtStageBoundary](../mtlcountersamplingpoint/atstageboundary.md) (see [- supportsCounterSampling:](<../mtldevice/supportscountersampling(__).md>)), set this property to [MTLCounterDontSample](../mtlcounterdontsample.md).

## See Also

### Configuring the sample buffer attachment

- [sampleBuffer](samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during a compute pass.
- [startOfEncoderSampleIndex](startofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the start of a compute pass.

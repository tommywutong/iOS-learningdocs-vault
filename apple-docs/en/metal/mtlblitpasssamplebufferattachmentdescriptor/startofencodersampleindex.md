---
title: startOfEncoderSampleIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex
source_url: 'https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.json'
content_hash: 'sha256:38d344902c031ce8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitPassSampleBufferAttachmentDescriptor](../mtlblitpasssamplebufferattachmentdescriptor.md)

# startOfEncoderSampleIndex

<sub>Instance Property</sub>

An index within a counter sample buffer that tells the GPU where to store counter data from the start of a blit pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var startOfEncoderSampleIndex: Int { get set }
```

## Discussion

This property indicates where the GPU stores the counter data within an [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md) instance that it samples at the beginning of a blit pass.

You can tell the GPU to skip sampling at the start of the blit pass by assigning [MTLCounterDontSample](../mtlcounterdontsample.md) to this property.

> [!important] Important
> For [MTLDevice](../mtldevice.md) instances that don’t support [MTLCounterSamplingPointAtStageBoundary](../mtlcountersamplingpoint/atstageboundary.md) (see [- supportsCounterSampling:](<../mtldevice/supportscountersampling(__).md>)), set this property to [MTLCounterDontSample](../mtlcounterdontsample.md).

## See Also

### Configuring the sample buffer attachment

- [sampleBuffer](samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during the blit pass.
- [endOfEncoderSampleIndex](endofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the end of a blit pass.

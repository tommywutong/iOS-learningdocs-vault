---
title: endOfEncoderSampleIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.json'
content_hash: 'sha256:da2d0b38fc87f2cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStatePassSampleBufferAttachmentDescriptor](../mtlresourcestatepasssamplebufferattachmentdescriptor.md)

# endOfEncoderSampleIndex

<sub>Instance Property</sub>

The index the Metal device object should use to store GPU counters when ending the resource state pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var endOfEncoderSampleIndex: Int { get set }
```

## Discussion

Specify [MTLCounterDontSample](../mtlcounterdontsample.md) if you don’t want to sample GPU counters at the end of the resource state pass. Otherwise, specify an index within the sample buffer where you want the GPU to write the sample data.

On devices that don’t support [MTLCounterSamplingPointAtStageBoundary](../mtlcountersamplingpoint/atstageboundary.md) you need to set the value to [MTLCounterDontSample](../mtlcounterdontsample.md).

## See Also

### Configuring the sample buffer attachment

- [sampleBuffer](samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during the resource state pass.
- [startOfEncoderSampleIndex](startofencodersampleindex.md) — The index the Metal device object should use to store GPU counters when starting the resource state pass.

---
title: startOfEncoderSampleIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex.json'
content_hash: 'sha256:a868c76813451012'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStatePassSampleBufferAttachmentDescriptor](../mtlresourcestatepasssamplebufferattachmentdescriptor.md)

# startOfEncoderSampleIndex

<sub>Instance Property</sub>

The index the Metal device object should use to store GPU counters when starting the resource state pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var startOfEncoderSampleIndex: Int { get set }
```

## Discussion

Specify [MTLCounterDontSample](../mtlcounterdontsample.md) if you don’t want to sample GPU counters at the start of the resource state pass. Otherwise, specify an index within the sample buffer where you want the GPU to write the sample data.

On devices that don’t support [MTLCounterSamplingPointAtStageBoundary](../mtlcountersamplingpoint/atstageboundary.md) you need to set the value to [MTLCounterDontSample](../mtlcounterdontsample.md).

## See Also

### Configuring the sample buffer attachment

- [sampleBuffer](samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during the resource state pass.
- [endOfEncoderSampleIndex](endofencodersampleindex.md) — The index the Metal device object should use to store GPU counters when ending the resource state pass.

---
title: MTLComputePassSampleBufferAttachmentDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor.json'
content_hash: 'sha256:0afc701d80f924c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLComputePassSampleBufferAttachmentDescriptor

<sub>Class</sub>

A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLComputePassSampleBufferAttachmentDescriptor
```

## Overview

For more context about configuring sample buffer attachments for compute passes, see [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md). That article is one of a series in [GPU counters and counter sample buffers](gpu-counters-and-counter-sample-buffers.md) about sampling Metal hardware counters for performance measurement.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the sample buffer attachment

- [sampleBuffer](mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during a compute pass.
- [startOfEncoderSampleIndex](mtlcomputepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the start of a compute pass.
- [endOfEncoderSampleIndex](mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the end of a compute pass.

## See Also

### Configuring a compute pass

- [MTLComputePassDescriptor](mtlcomputepassdescriptor.md) — A description of how to dispatch execution of pass commands and GPU performance sampling.
- [MTLDispatchType](mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
- [MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepasssamplebufferattachmentdescriptorarray.md) — A container that stores an array of sample buffer attachments for a compute pass.

---
title: MTLBlitPassSampleBufferAttachmentDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitpasssamplebufferattachmentdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitpasssamplebufferattachmentdescriptor.json'
content_hash: 'sha256:7542ad9a7bd16eef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBlitPassSampleBufferAttachmentDescriptor

<sub>Class</sub>

A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLBlitPassSampleBufferAttachmentDescriptor
```

## Overview

See [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) for more context about configuring instances of this type. That article is one of a series of articles in [GPU counters and counter sample buffers](gpu-counters-and-counter-sample-buffers.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the sample buffer attachment

- [sampleBuffer](mtlblitpasssamplebufferattachmentdescriptor/samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during the blit pass.
- [startOfEncoderSampleIndex](mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the start of a blit pass.
- [endOfEncoderSampleIndex](mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex.md) — An index within a counter sample buffer that tells the GPU where to store counter data from the end of a blit pass.

## See Also

### Configuring a blit command encoder

- [MTLBlitPassDescriptor](mtlblitpassdescriptor.md) — A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.
- [MTLBlitPassSampleBufferAttachmentDescriptorArray](mtlblitpasssamplebufferattachmentdescriptorarray.md) — A container that stores an array of sample buffer attachments for a blit pass.

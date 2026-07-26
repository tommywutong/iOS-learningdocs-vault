---
title: MTLComputePassDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepassdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepassdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepassdescriptor.json'
content_hash: 'sha256:119de4fac8bebf61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLComputePassDescriptor

<sub>Class</sub>

A description of how to dispatch execution of pass commands and GPU performance sampling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLComputePassDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the dispatch mechanism

- [dispatchType](mtlcomputepassdescriptor/dispatchtype.md) — The strategy for dispatching any compute commands encoded in the compute pass.

### Specifying sample buffers for GPU counters

- [sampleBufferAttachments](mtlcomputepassdescriptor/samplebufferattachments.md) — The sample buffers that the compute pass can access.

## See Also

### Configuring a compute pass

- [MTLDispatchType](mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
- [MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md) — A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.
- [MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepasssamplebufferattachmentdescriptorarray.md) — A container that stores an array of sample buffer attachments for a compute pass.

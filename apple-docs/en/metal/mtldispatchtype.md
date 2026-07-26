---
title: MTLDispatchType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldispatchtype
source_url: 'https://developer.apple.com/documentation/metal/mtldispatchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldispatchtype.json'
content_hash: 'sha256:7309e2608d67e4bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDispatchType

<sub>Enumeration</sub>

The type of dispatch method to use when calling encoded functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLDispatchType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Execution dispatch types

- [MTLDispatchTypeConcurrent](mtldispatchtype/concurrent.md) — Sets a command encoder to dispatch encoded commands concurrently during your pass.
- [MTLDispatchTypeSerial](mtldispatchtype/serial.md) — Sets a command encoder to dispatch encoded commands serially during your pass.

### Initializers

- [init(rawValue:)](<mtldispatchtype/init(rawvalue_).md>)

## See Also

### Configuring a compute pass

- [MTLComputePassDescriptor](mtlcomputepassdescriptor.md) — A description of how to dispatch execution of pass commands and GPU performance sampling.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
- [MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md) — A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.
- [MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepasssamplebufferattachmentdescriptorarray.md) — A container that stores an array of sample buffer attachments for a compute pass.

---
title: MTLComputePassSampleBufferAttachmentDescriptorArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray.json'
content_hash: 'sha256:f86523de03eaaab0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLComputePassSampleBufferAttachmentDescriptorArray

<sub>Class</sub>

A container that stores an array of sample buffer attachments for a compute pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLComputePassSampleBufferAttachmentDescriptorArray
```

## Overview

The number of elements in the array is at least the number of elements in an [MTLDevice](mtldevice.md) instance’s [counterSets](mtldevice/countersets.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing a sample buffer attachment

- [- objectAtIndexedSubscript:](<mtlcomputepasssamplebufferattachmentdescriptorarray/subscript(__).md>) — Returns the descriptor object for the specified sample buffer attachment.

## See Also

### Configuring a compute pass

- [MTLComputePassDescriptor](mtlcomputepassdescriptor.md) — A description of how to dispatch execution of pass commands and GPU performance sampling.
- [MTLDispatchType](mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
- [MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md) — A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.

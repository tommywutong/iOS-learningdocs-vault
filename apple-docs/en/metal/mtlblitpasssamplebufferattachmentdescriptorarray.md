---
title: MTLBlitPassSampleBufferAttachmentDescriptorArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray
source_url: 'https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray.json'
content_hash: 'sha256:5fe3e4b3d40598c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBlitPassSampleBufferAttachmentDescriptorArray

<sub>Class</sub>

A container that stores an array of sample buffer attachments for a blit pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLBlitPassSampleBufferAttachmentDescriptorArray
```

## Overview

The number of elements in the array is at least the number of elements in an [MTLDevice](mtldevice.md) instance’s [counterSets](mtldevice/countersets.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing a sample buffer attachment descriptor

- [- objectAtIndexedSubscript:](<mtlblitpasssamplebufferattachmentdescriptorarray/subscript(__).md>) — Accesses one of the array’s blit pass sample buffer attachment descriptor instances.

## See Also

### Configuring a blit command encoder

- [MTLBlitPassDescriptor](mtlblitpassdescriptor.md) — A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.
- [MTLBlitPassSampleBufferAttachmentDescriptor](mtlblitpasssamplebufferattachmentdescriptor.md) — A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.

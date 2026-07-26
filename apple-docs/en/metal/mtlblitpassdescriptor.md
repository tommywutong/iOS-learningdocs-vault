---
title: MTLBlitPassDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitpassdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlblitpassdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitpassdescriptor.json'
content_hash: 'sha256:07be561af6bb8270'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBlitPassDescriptor

<sub>Class</sub>

A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLBlitPassDescriptor
```

## Overview

You can customize an encoder for a blit pass by creating and configuring an [MTLBlitPassDescriptor](mtlblitpassdescriptor.md) instance and passing it to [- blitCommandEncoderWithDescriptor:](<mtlcommandbuffer/makeblitcommandencoder(descriptor_).md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring sample buffer attachment descriptors for a blit pass

- [sampleBufferAttachments](mtlblitpassdescriptor/samplebufferattachments.md) — An array of counter sample buffer attachments that you configure for a blit pass.

## See Also

### Configuring a blit command encoder

- [MTLBlitPassSampleBufferAttachmentDescriptor](mtlblitpasssamplebufferattachmentdescriptor.md) — A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.
- [MTLBlitPassSampleBufferAttachmentDescriptorArray](mtlblitpasssamplebufferattachmentdescriptorarray.md) — A container that stores an array of sample buffer attachments for a blit pass.

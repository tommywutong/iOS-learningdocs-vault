---
title: MTLTensorBufferAttachments
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensorbufferattachments
source_url: 'https://developer.apple.com/documentation/metal/mtltensorbufferattachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorbufferattachments.json'
content_hash: 'sha256:22702b8507c20bdf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorBufferAttachments

<sub>Class</sub>

An object that associates each plane of a tensor with a buffer and byte offset for buffer-backed tensor creation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTensorBufferAttachments
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- bufferForPlane:](<mtltensorbufferattachments/buffer(for_).md>) — Returns the buffer backing the given plane, or `nil` if none has been set. _(beta)_
- [- offsetForPlane:](<mtltensorbufferattachments/offset(for_).md>) — Returns the byte offset into the buffer for the given plane. _(beta)_
- [- reset](<mtltensorbufferattachments/reset().md>) — Empties the container of all its elements. _(beta)_
- [- setBuffer:offset:forPlane:](<mtltensorbufferattachments/setbuffer(__offset_for_).md>) — Sets the buffer and byte offset to use as backing storage for the given plane. _(beta)_

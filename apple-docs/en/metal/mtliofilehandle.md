---
title: MTLIOFileHandle
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliofilehandle
source_url: 'https://developer.apple.com/documentation/metal/mtliofilehandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliofilehandle.json'
content_hash: 'sha256:fd2fb553c534f088'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOFileHandle

<sub>Protocol</sub>

Represents a raw or compressed file, such as a resource asset file in your app’s bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIOFileHandle : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Naming a file handle

- [label](mtliofilehandle/label.md) — An optional name for the file that the handle represents.

## See Also

### I/O command buffers

- [MTLIOCommandBuffer](mtliocommandbuffer.md) — A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [MTLIOCommandBufferHandler](mtliocommandbufferhandler.md) — A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [MTLIOStatus](mtliostatus.md) — Represents the state of an input/output command buffer.
- [Code](mtlioerror-swift.struct/code.md) — The error codes for creating an input/output file handle.
- [MTLIOErrorDomain](mtlioerrordomain.md) — The domain for input/output command queue errors.

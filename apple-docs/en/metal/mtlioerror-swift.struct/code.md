---
title: MTLIOError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlioerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtlioerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlioerror-swift.struct/code.json'
content_hash: 'sha256:cee706ae64fe15f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOError](../mtlioerror-swift.struct.md)

# MTLIOError.Code

<sub>Enumeration</sub>

The error codes for creating an input/output file handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error codes

- [MTLIOErrorURLInvalid](code/urlinvalid.md) — An error code that represents a problem with a file URL.
- [MTLIOErrorInternal](code/internal.md) — An error code that represents a problem internal to the Metal framework.
- [MTLIOErrorURLInvalid](code/urlinvalid.md) — An error code that represents a problem with a file URL.
- [MTLIOErrorInternal](code/internal.md) — An error code that represents a problem internal to the Metal framework.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### I/O command buffers

- [MTLIOCommandBuffer](../mtliocommandbuffer.md) — A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [MTLIOFileHandle](../mtliofilehandle.md) — Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [MTLIOCommandBufferHandler](../mtliocommandbufferhandler.md) — A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [MTLIOStatus](../mtliostatus.md) — Represents the state of an input/output command buffer.
- [MTLIOErrorDomain](../mtlioerrordomain.md) — The domain for input/output command queue errors.

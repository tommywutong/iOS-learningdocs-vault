---
title: MTLIOStatus
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliostatus
source_url: 'https://developer.apple.com/documentation/metal/mtliostatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliostatus.json'
content_hash: 'sha256:beada0fe0148f1de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOStatus

<sub>Enumeration</sub>

Represents the state of an input/output command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLIOStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### I/O command queue states

- [MTLIOStatusPending](mtliostatus/pending.md) — Indicates the GPU hasn’t finished executing the input/output command buffer.
- [MTLIOStatusComplete](mtliostatus/complete.md) — Indicates the GPU has successfully finished executing the input/output command buffer.
- [MTLIOStatusCancelled](mtliostatus/cancelled.md) — Indicates the GPU has successfully abandoned the input/output command buffer.
- [MTLIOStatusError](mtliostatus/error.md) — Indicates the GPU experienced a problem with the input/output command buffer.

### Initializers

- [init(rawValue:)](<mtliostatus/init(rawvalue_).md>)

## See Also

### I/O command buffers

- [MTLIOCommandBuffer](mtliocommandbuffer.md) — A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [MTLIOFileHandle](mtliofilehandle.md) — Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [MTLIOCommandBufferHandler](mtliocommandbufferhandler.md) — A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [Code](mtlioerror-swift.struct/code.md) — The error codes for creating an input/output file handle.
- [MTLIOErrorDomain](mtlioerrordomain.md) — The domain for input/output command queue errors.

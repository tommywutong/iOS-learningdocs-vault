---
title: MTLIOCommandBufferHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbufferhandler
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbufferhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbufferhandler.json'
content_hash: 'sha256:ad4f4b02d6cf684e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCommandBufferHandler

<sub>Type Alias</sub>

A convenience type that defines the signature of an input/output command buffer’s completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLIOCommandBufferHandler = @Sendable (any MTLIOCommandBuffer) -> Void
```

## Parameters

- `inputOutputCommandBuffer` — The [MTLIOCommandBuffer](mtliocommandbuffer.md) instance that has finished executing is calling your completion handler.

## See Also

### I/O command buffers

- [MTLIOCommandBuffer](mtliocommandbuffer.md) — A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [MTLIOFileHandle](mtliofilehandle.md) — Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [MTLIOStatus](mtliostatus.md) — Represents the state of an input/output command buffer.
- [Code](mtlioerror-swift.struct/code.md) — The error codes for creating an input/output file handle.
- [MTLIOErrorDomain](mtlioerrordomain.md) — The domain for input/output command queue errors.

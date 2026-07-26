---
title: MTLIOErrorDomain
framework: Metal
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlioerrordomain
source_url: 'https://developer.apple.com/documentation/metal/mtlioerrordomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlioerrordomain.json'
content_hash: 'sha256:c56c4f78445faa8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOErrorDomain

<sub>Global Variable</sub>

The domain for input/output command queue errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let MTLIOErrorDomain: String
```

## See Also

### I/O command buffers

- [MTLIOCommandBuffer](mtliocommandbuffer.md) — A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [MTLIOFileHandle](mtliofilehandle.md) — Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [MTLIOCommandBufferHandler](mtliocommandbufferhandler.md) — A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [MTLIOStatus](mtliostatus.md) — Represents the state of an input/output command buffer.
- [Code](mtlioerror-swift.struct/code.md) — The error codes for creating an input/output file handle.

---
title: error
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer/error
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/error.json'
content_hash: 'sha256:3d50599b6386328a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# error

<sub>Instance Property</sub>

Stores the details of an error when the GPU experienced a problem with the input/output command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## See Also

### Checking the state of a command buffer

- [status](status.md) — Represents the state of the input/output command buffer.

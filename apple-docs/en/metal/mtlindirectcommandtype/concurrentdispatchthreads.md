---
title: concurrentDispatchThreads
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandtype/concurrentdispatchthreads
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandtype/concurrentdispatchthreads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandtype/concurrentdispatchthreads.json'
content_hash: 'sha256:d173b21685e2631d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandType](../mtlindirectcommandtype.md)

# concurrentDispatchThreads

<sub>Type Property</sub>

A compute command using an arbitrarily sized grid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var concurrentDispatchThreads: MTLIndirectCommandType { get }
```

## See Also

### Specifying command types

- [MTLIndirectCommandTypeDraw](draw.md) — A draw call command.
- [MTLIndirectCommandTypeDrawIndexed](drawindexed.md) — An indexed draw call command.
- [MTLIndirectCommandTypeDrawPatches](drawpatches.md) — A draw call command for tessellated patches.
- [MTLIndirectCommandTypeDrawIndexedPatches](drawindexedpatches.md) — An indexed draw call command for tessellated patches.
- [MTLIndirectCommandTypeConcurrentDispatch](concurrentdispatch.md) — A compute command using a grid aligned to threadgroup boundaries.

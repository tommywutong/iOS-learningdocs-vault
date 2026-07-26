---
title: concurrentDispatch
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandtype/concurrentdispatch
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandtype/concurrentdispatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandtype/concurrentdispatch.json'
content_hash: 'sha256:6c7d6d524c6aa02f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandType](../mtlindirectcommandtype.md)

# concurrentDispatch

<sub>Type Property</sub>

A compute command using a grid aligned to threadgroup boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var concurrentDispatch: MTLIndirectCommandType { get }
```

## See Also

### Specifying command types

- [MTLIndirectCommandTypeDraw](draw.md) — A draw call command.
- [MTLIndirectCommandTypeDrawIndexed](drawindexed.md) — An indexed draw call command.
- [MTLIndirectCommandTypeDrawPatches](drawpatches.md) — A draw call command for tessellated patches.
- [MTLIndirectCommandTypeDrawIndexedPatches](drawindexedpatches.md) — An indexed draw call command for tessellated patches.
- [MTLIndirectCommandTypeConcurrentDispatchThreads](concurrentdispatchthreads.md) — A compute command using an arbitrarily sized grid.

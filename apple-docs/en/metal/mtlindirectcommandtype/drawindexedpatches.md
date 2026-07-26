---
title: drawIndexedPatches
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandtype/drawindexedpatches
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandtype/drawindexedpatches'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandtype/drawindexedpatches.json'
content_hash: 'sha256:cacdab32299dda64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandType](../mtlindirectcommandtype.md)

# drawIndexedPatches

<sub>Type Property</sub>

An indexed draw call command for tessellated patches.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var drawIndexedPatches: MTLIndirectCommandType { get }
```

## See Also

### Specifying command types

- [MTLIndirectCommandTypeDraw](draw.md) — A draw call command.
- [MTLIndirectCommandTypeDrawIndexed](drawindexed.md) — An indexed draw call command.
- [MTLIndirectCommandTypeDrawPatches](drawpatches.md) — A draw call command for tessellated patches.
- [MTLIndirectCommandTypeConcurrentDispatch](concurrentdispatch.md) — A compute command using a grid aligned to threadgroup boundaries.
- [MTLIndirectCommandTypeConcurrentDispatchThreads](concurrentdispatchthreads.md) — A compute command using an arbitrarily sized grid.

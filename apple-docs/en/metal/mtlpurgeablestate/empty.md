---
title: MTLPurgeableState.empty
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpurgeablestate/empty
source_url: 'https://developer.apple.com/documentation/metal/mtlpurgeablestate/empty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpurgeablestate/empty.json'
content_hash: 'sha256:8c6cb98160502f81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPurgeableState](../mtlpurgeablestate.md)

# MTLPurgeableState.empty

<sub>Case</sub>

A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case empty
```

## See Also

### Specifying purgeable states

- [MTLPurgeableStateKeepCurrent](keepcurrent.md) — The current state is queried but doesn’t change.
- [MTLPurgeableStateNonVolatile](nonvolatile.md) — The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableStateVolatile](volatile.md) — The system is allowed to discard the resource to free up memory.

---
title: MTLPurgeableState.volatile
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpurgeablestate/volatile
source_url: 'https://developer.apple.com/documentation/metal/mtlpurgeablestate/volatile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpurgeablestate/volatile.json'
content_hash: 'sha256:c9666b0b3c24ec18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPurgeableState](../mtlpurgeablestate.md)

# MTLPurgeableState.volatile

<sub>Case</sub>

The system is allowed to discard the resource to free up memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case volatile
```

## See Also

### Specifying purgeable states

- [MTLPurgeableStateKeepCurrent](keepcurrent.md) — The current state is queried but doesn’t change.
- [MTLPurgeableStateNonVolatile](nonvolatile.md) — The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableStateEmpty](empty.md) — A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.

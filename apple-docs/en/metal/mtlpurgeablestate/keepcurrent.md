---
title: MTLPurgeableState.keepCurrent
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpurgeablestate/keepcurrent
source_url: 'https://developer.apple.com/documentation/metal/mtlpurgeablestate/keepcurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpurgeablestate/keepcurrent.json'
content_hash: 'sha256:9d1107c74db0aaab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPurgeableState](../mtlpurgeablestate.md)

# MTLPurgeableState.keepCurrent

<sub>Case</sub>

The current state is queried but doesn’t change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case keepCurrent
```

## Discussion

The [- setPurgeableState:](<../mtlresource/setpurgeablestate(__).md>) method never returns this value. When this value is passed to that function, it returns the current purgability state without changing it.

## See Also

### Specifying purgeable states

- [MTLPurgeableStateNonVolatile](nonvolatile.md) — The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableStateVolatile](volatile.md) — The system is allowed to discard the resource to free up memory.
- [MTLPurgeableStateEmpty](empty.md) — A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.

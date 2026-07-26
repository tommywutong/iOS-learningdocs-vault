---
title: MTLPurgeableState
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpurgeablestate
source_url: 'https://developer.apple.com/documentation/metal/mtlpurgeablestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpurgeablestate.json'
content_hash: 'sha256:89fd0fe7871227b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPurgeableState

<sub>Enumeration</sub>

The purgeable state of the resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLPurgeableState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying purgeable states

- [MTLPurgeableStateKeepCurrent](mtlpurgeablestate/keepcurrent.md) — The current state is queried but doesn’t change.
- [MTLPurgeableStateNonVolatile](mtlpurgeablestate/nonvolatile.md) — The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableStateVolatile](mtlpurgeablestate/volatile.md) — The system is allowed to discard the resource to free up memory.
- [MTLPurgeableStateEmpty](mtlpurgeablestate/empty.md) — A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.

### Initializers

- [init(rawValue:)](<mtlpurgeablestate/init(rawvalue_).md>)

## See Also

### Setting the purgeable state of the resource

- [- setPurgeableState:](<mtlresource/setpurgeablestate(__).md>) — Specifies or queries the resource’s purgeable state.

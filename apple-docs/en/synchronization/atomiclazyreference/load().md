---
title: load()
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomiclazyreference/load()
source_url: 'https://developer.apple.com/documentation/synchronization/atomiclazyreference/load()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomiclazyreference/load%28%29.json'
content_hash: 'sha256:6004ec9ef9a54333'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicLazyReference](../atomiclazyreference.md)

# load()

<sub>Instance Method</sub>

Atomically loads and returns the current value of this reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load() -> Instance?
```

## Return Value

A value of `Instance` if the lazy reference was written to, or `nil` if it has not been written to yet.

## Discussion

> [!note] Note
> The load operation is performed with the memory ordering `AtomicLoadOrdering.acquiring`.

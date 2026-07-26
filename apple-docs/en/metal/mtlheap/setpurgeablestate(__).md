---
title: 'setPurgeableState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlheap/setpurgeablestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/setpurgeablestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/setpurgeablestate%28_%3A%29.json'
content_hash: 'sha256:3dde23748a494224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# setPurgeableState(_:)

<sub>Instance Method</sub>

Sets the purgeable state of the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setPurgeableState(_ state: MTLPurgeableState) -> MTLPurgeableState
```

## Parameters

- `state` — The desired purgeable state of the heap.

## Return Value

The previous purgeable state of the heap.

## Discussion

The heap purgeability state refers to its whole backing memory and affects all resources in the heap. Heaps can be marked purgeable but its resources cannot; the heap’s resources always reflect the heap’s purgeability state.

Refer to the [MTLPurgeableState](../mtlpurgeablestate.md) and [- setPurgeableState:](<../mtlresource/setpurgeablestate(__).md>) reference for further information.

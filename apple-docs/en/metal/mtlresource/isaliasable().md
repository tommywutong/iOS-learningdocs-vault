---
title: isAliasable()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresource/isaliasable()
source_url: 'https://developer.apple.com/documentation/metal/mtlresource/isaliasable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresource/isaliasable%28%29.json'
content_hash: 'sha256:256af24bc7875acc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResource](../mtlresource.md)

# isAliasable()

<sub>Instance Method</sub>

A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func isAliasable() -> Bool
```

## Return Value

The default value is [false](../../swift/false.md). The value is [true](../../swift/true.md) only if the [- makeAliasable](<makealiasable().md>) method was previously called on this resource.

## See Also

### Managing heap resources

- [heapOffset](heapoffset.md) — The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.
- [heap](heap.md) — The heap on which the resource is allocated, if any.
- [- makeAliasable](<makealiasable().md>) — Allows future heap resource allocations to alias against the resource’s memory, reusing it.

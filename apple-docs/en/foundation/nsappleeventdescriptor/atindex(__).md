---
title: 'atIndex(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/atindex(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/atindex(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/atindex%28_%3A%29.json'
content_hash: 'sha256:b1a91e649a5045a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# atIndex(_:)

<sub>Instance Method</sub>

Returns the descriptor at the specified (one-based) position in the receiving descriptor list.

<sub>Mac Catalyst, macOS</sub>

```swift
func atIndex(_ index: Int) -> NSAppleEventDescriptor?
```

## Parameters

- `index` — The one-based descriptor list position of the descriptor to return.

## Return Value

The descriptor from the specified position (one-based) in the descriptor list, or `nil` if the specified descriptor cannot be obtained.

## See Also

### Working With List Descriptors

- [- insertDescriptor:atIndex:](<insert(__at_).md>) — Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.
- [- removeDescriptorAtIndex:](<remove(at_).md>) — Removes the descriptor at the specified (one-based) position in the receiving descriptor list.

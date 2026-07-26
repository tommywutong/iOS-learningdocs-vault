---
title: 'remove(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/remove(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/remove(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/remove%28at%3A%29.json'
content_hash: 'sha256:236c9acc957eece9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# remove(at:)

<sub>Instance Method</sub>

Removes the descriptor at the specified (one-based) position in the receiving descriptor list.

<sub>Mac Catalyst, macOS</sub>

```swift
func remove(at index: Int)
```

## Parameters

- `index` — The one-based position of the descriptor to remove.

## Discussion

The receiver must be a list descriptor. The  indices are one-based. Currently provides no indication if an error occurs.

## See Also

### Working With List Descriptors

- [- descriptorAtIndex:](<atindex(__).md>) — Returns the descriptor at the specified (one-based) position in the receiving descriptor list.
- [- insertDescriptor:atIndex:](<insert(__at_).md>) — Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.

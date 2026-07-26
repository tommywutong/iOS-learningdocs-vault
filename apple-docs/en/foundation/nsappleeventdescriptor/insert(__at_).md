---
title: 'insert(_:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/insert(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/insert(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/insert%28_%3Aat%3A%29.json'
content_hash: 'sha256:2f107815d5fada15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.

<sub>Mac Catalyst, macOS</sub>

```swift
func insert(_ descriptor: NSAppleEventDescriptor, at index: Int)
```

## Parameters

- `descriptor` — The descriptor to insert in the receiver. Specifying an index of 0 or count + 1 causes appending to the end of the list.

- `index` — The one-based descriptor list position at which to insert the descriptor.

## Discussion

Because it actually replaces the descriptor, if any, at the specified position, this method might better be called `replaceDescriptor:atIndex:`. The receiver must be a list descriptor. The indices are one-based. Currently provides no indication if an error occurs.

## See Also

### Working With List Descriptors

- [- descriptorAtIndex:](<atindex(__).md>) — Returns the descriptor at the specified (one-based) position in the receiving descriptor list.
- [- removeDescriptorAtIndex:](<remove(at_).md>) — Removes the descriptor at the specified (one-based) position in the receiving descriptor list.

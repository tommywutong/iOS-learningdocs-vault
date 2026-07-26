---
title: 'keywordForDescriptor(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/keywordfordescriptor(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/keywordfordescriptor(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/keywordfordescriptor%28at%3A%29.json'
content_hash: 'sha256:6d3adf37829745e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# keywordForDescriptor(at:)

<sub>Instance Method</sub>

Returns the keyword for the descriptor at the specified (one-based) position in the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func keywordForDescriptor(at index: Int) -> AEKeyword
```

## Parameters

- `index` — The one-based descriptor list position of the descriptor to get the keyword for.

## Return Value

The keyword (a four-character code) for the descriptor at the one-based location specified by `anIndex`, or 0 if an error occurs.

## See Also

### Working With Record Descriptors

- [- descriptorForKeyword:](<forkeyword(__).md>) — Returns the receiver’s descriptor for the specified keyword.
- [- removeDescriptorWithKeyword:](<remove(withkeyword_).md>) — Removes the receiver’s descriptor identified by the specified keyword.
- [- setDescriptor:forKeyword:](<setdescriptor(__forkeyword_).md>) — Adds a descriptor, identified by a keyword, to the receiver.

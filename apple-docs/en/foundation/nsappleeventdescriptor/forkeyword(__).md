---
title: 'forKeyword(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/forkeyword(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/forkeyword(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/forkeyword%28_%3A%29.json'
content_hash: 'sha256:86f195ecfe9fb835'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# forKeyword(_:)

<sub>Instance Method</sub>

Returns the receiver’s descriptor for the specified keyword.

<sub>Mac Catalyst, macOS</sub>

```swift
func forKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor?
```

## Parameters

- `keyword` — A keyword (a four-character code) that identifies the descriptor to obtain.

## Return Value

A descriptor for the specified keyword, or `nil` if an error occurs.

## See Also

### Working With Record Descriptors

- [- keywordForDescriptorAtIndex:](<keywordfordescriptor(at_).md>) — Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [- removeDescriptorWithKeyword:](<remove(withkeyword_).md>) — Removes the receiver’s descriptor identified by the specified keyword.
- [- setDescriptor:forKeyword:](<setdescriptor(__forkeyword_).md>) — Adds a descriptor, identified by a keyword, to the receiver.

---
title: 'remove(withKeyword:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/remove(withkeyword:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/remove(withkeyword:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/remove%28withkeyword%3A%29.json'
content_hash: 'sha256:f7e7380118c68337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# remove(withKeyword:)

<sub>Instance Method</sub>

Removes the receiver’s descriptor identified by the specified keyword.

<sub>Mac Catalyst, macOS</sub>

```swift
func remove(withKeyword keyword: AEKeyword)
```

## Parameters

- `keyword` — A keyword (a four-character code) that identifies the descriptor to remove.

## Discussion

The receiver must be an Apple event or Apple event record. Currently provides no indication if an error occurs.

## See Also

### Working With Record Descriptors

- [- descriptorForKeyword:](<forkeyword(__).md>) — Returns the receiver’s descriptor for the specified keyword.
- [- keywordForDescriptorAtIndex:](<keywordfordescriptor(at_).md>) — Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [- setDescriptor:forKeyword:](<setdescriptor(__forkeyword_).md>) — Adds a descriptor, identified by a keyword, to the receiver.

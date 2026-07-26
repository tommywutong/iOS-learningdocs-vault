---
title: 'setDescriptor(_:forKeyword:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/setdescriptor(_:forkeyword:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/setdescriptor(_:forkeyword:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/setdescriptor%28_%3Aforkeyword%3A%29.json'
content_hash: 'sha256:122bf987a0640853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# setDescriptor(_:forKeyword:)

<sub>Instance Method</sub>

Adds a descriptor, identified by a keyword, to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func setDescriptor(_ descriptor: NSAppleEventDescriptor, forKeyword keyword: AEKeyword)
```

## Parameters

- `descriptor` — The descriptor to add to the receiver.

- `keyword` — A keyword (a four-character code) that identifies the descriptor to add. If a descriptor with that keyword already exists in the receiver, it is replaced.

## Discussion

The receiver must be an Apple event or Apple event record. Currently provides no indication if an error occurs.

## See Also

### Working With Record Descriptors

- [- descriptorForKeyword:](<forkeyword(__).md>) — Returns the receiver’s descriptor for the specified keyword.
- [- keywordForDescriptorAtIndex:](<keywordfordescriptor(at_).md>) — Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [- removeDescriptorWithKeyword:](<remove(withkeyword_).md>) — Removes the receiver’s descriptor identified by the specified keyword.

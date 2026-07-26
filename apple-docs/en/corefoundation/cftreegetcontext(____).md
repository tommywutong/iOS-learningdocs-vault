---
title: 'CFTreeGetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreegetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreegetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreegetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:d0252b97e190abfc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeGetContext(_:_:)

<sub>Function</sub>

Returns the context of the specified tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeGetContext(_ tree: CFTree!, _ context: UnsafeMutablePointer<CFTreeContext>!)
```

## Parameters

- `tree` — The tree to examine.

- `context` — The [CFTreeContext](cftreecontext.md) structure to be filled in with the context of the specified tree. This value must be a valid C pointer to a [CFTreeContext](cftreecontext.md) structure-sized block of storage. If the version number of the storage is not a valid [CFTreeContext](cftreecontext.md) structure version number, the result is undefined.

## See Also

### Examining a Tree

- [CFTreeFindRoot](<cftreefindroot(__).md>) — Returns the root tree of a given tree.
- [CFTreeGetChildAtIndex](<cftreegetchildatindex(____).md>) — Returns the child of a tree at the specified index.
- [CFTreeGetChildCount](<cftreegetchildcount(__).md>) — Returns the number of children in a tree.
- [CFTreeGetChildren](<cftreegetchildren(____).md>) — Fills a buffer with children from the tree.
- [CFTreeGetFirstChild](<cftreegetfirstchild(__).md>) — Returns the first child of a tree.
- [CFTreeGetNextSibling](<cftreegetnextsibling(__).md>) — Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [CFTreeGetParent](<cftreegetparent(__).md>) — Returns the parent of a given tree.

---
title: 'CFTreeGetNextSibling(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreegetnextsibling(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreegetnextsibling(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreegetnextsibling%28_%3A%29.json'
content_hash: 'sha256:8baa91528f2635cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeGetNextSibling(_:)

<sub>Function</sub>

Returns the next sibling, adjacent to a given tree, in the parent’s children list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeGetNextSibling(_ tree: CFTree!) -> CFTree!
```

## Parameters

- `tree` — The tree to examine.

## Return Value

The next sibling, adjacent to `tree`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a Tree

- [CFTreeFindRoot](<cftreefindroot(__).md>) — Returns the root tree of a given tree.
- [CFTreeGetChildAtIndex](<cftreegetchildatindex(____).md>) — Returns the child of a tree at the specified index.
- [CFTreeGetChildCount](<cftreegetchildcount(__).md>) — Returns the number of children in a tree.
- [CFTreeGetChildren](<cftreegetchildren(____).md>) — Fills a buffer with children from the tree.
- [CFTreeGetContext](<cftreegetcontext(____).md>) — Returns the context of the specified tree.
- [CFTreeGetFirstChild](<cftreegetfirstchild(__).md>) — Returns the first child of a tree.
- [CFTreeGetParent](<cftreegetparent(__).md>) — Returns the parent of a given tree.

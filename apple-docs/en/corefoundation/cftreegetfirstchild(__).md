---
title: 'CFTreeGetFirstChild(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreegetfirstchild(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreegetfirstchild(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreegetfirstchild%28_%3A%29.json'
content_hash: 'sha256:8927b9ad9c2bcfbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeGetFirstChild(_:)

<sub>Function</sub>

Returns the first child of a tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeGetFirstChild(_ tree: CFTree!) -> CFTree!
```

## Parameters

- `tree` — The tree to examine.

## Return Value

The first child of `tree`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a Tree

- [CFTreeFindRoot](<cftreefindroot(__).md>) — Returns the root tree of a given tree.
- [CFTreeGetChildAtIndex](<cftreegetchildatindex(____).md>) — Returns the child of a tree at the specified index.
- [CFTreeGetChildCount](<cftreegetchildcount(__).md>) — Returns the number of children in a tree.
- [CFTreeGetChildren](<cftreegetchildren(____).md>) — Fills a buffer with children from the tree.
- [CFTreeGetContext](<cftreegetcontext(____).md>) — Returns the context of the specified tree.
- [CFTreeGetNextSibling](<cftreegetnextsibling(__).md>) — Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [CFTreeGetParent](<cftreegetparent(__).md>) — Returns the parent of a given tree.

---
title: 'CFTreeGetChildAtIndex(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreegetchildatindex(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreegetchildatindex(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreegetchildatindex%28_%3A_%3A%29.json'
content_hash: 'sha256:baa5c1d42b2c6b5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeGetChildAtIndex(_:_:)

<sub>Function</sub>

Returns the child of a tree at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeGetChildAtIndex(_ tree: CFTree!, _ idx: CFIndex) -> CFTree!
```

## Parameters

- `tree` — The tree to examine.

- `idx` — The index of the child obtain. The value must be less than the number of children in `tree`.

## Return Value

The child tree at `idx`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a Tree

- [CFTreeFindRoot](<cftreefindroot(__).md>) — Returns the root tree of a given tree.
- [CFTreeGetChildCount](<cftreegetchildcount(__).md>) — Returns the number of children in a tree.
- [CFTreeGetChildren](<cftreegetchildren(____).md>) — Fills a buffer with children from the tree.
- [CFTreeGetContext](<cftreegetcontext(____).md>) — Returns the context of the specified tree.
- [CFTreeGetFirstChild](<cftreegetfirstchild(__).md>) — Returns the first child of a tree.
- [CFTreeGetNextSibling](<cftreegetnextsibling(__).md>) — Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [CFTreeGetParent](<cftreegetparent(__).md>) — Returns the parent of a given tree.

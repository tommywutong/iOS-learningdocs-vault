---
title: 'CFTreeGetChildCount(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreegetchildcount(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreegetchildcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreegetchildcount%28_%3A%29.json'
content_hash: 'sha256:10c258d307aec9ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeGetChildCount(_:)

<sub>Function</sub>

Returns the number of children in a tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeGetChildCount(_ tree: CFTree!) -> CFIndex
```

## Parameters

- `tree` — The tree to examine.

## Return Value

The number of children in `tree`.

## See Also

### Examining a Tree

- [CFTreeFindRoot](<cftreefindroot(__).md>) — Returns the root tree of a given tree.
- [CFTreeGetChildAtIndex](<cftreegetchildatindex(____).md>) — Returns the child of a tree at the specified index.
- [CFTreeGetChildren](<cftreegetchildren(____).md>) — Fills a buffer with children from the tree.
- [CFTreeGetContext](<cftreegetcontext(____).md>) — Returns the context of the specified tree.
- [CFTreeGetFirstChild](<cftreegetfirstchild(__).md>) — Returns the first child of a tree.
- [CFTreeGetNextSibling](<cftreegetnextsibling(__).md>) — Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [CFTreeGetParent](<cftreegetparent(__).md>) — Returns the parent of a given tree.

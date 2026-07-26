---
title: 'CFTreeRemove(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreeremove(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreeremove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreeremove%28_%3A%29.json'
content_hash: 'sha256:9fe434d4c9f832e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeRemove(_:)

<sub>Function</sub>

Removes a tree from its parent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeRemove(_ tree: CFTree!)
```

## Parameters

- `tree` — The tree to remove from its parent.

## Discussion

When a child tree is removed from its parent, the parent releases it. If you want to use the child after you have removed it, you should ensure you retain it before removing it from its parent.

## See Also

### Modifying a Tree

- [CFTreeAppendChild](<cftreeappendchild(____).md>) — Adds a new child to a tree as the last in its list of children.
- [CFTreeInsertSibling](<cftreeinsertsibling(____).md>) — Inserts a new sibling after a given tree.
- [CFTreeRemoveAllChildren](<cftreeremoveallchildren(__).md>) — Removes all the children of a tree.
- [CFTreePrependChild](<cftreeprependchild(____).md>) — Adds a new child to the specified tree as the first in its list of children.
- [CFTreeSetContext](<cftreesetcontext(____).md>) — Replaces the context of a tree by releasing the old information pointer and retaining the new one.

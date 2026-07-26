---
title: 'CFTreeInsertSibling(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreeinsertsibling(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreeinsertsibling(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreeinsertsibling%28_%3A_%3A%29.json'
content_hash: 'sha256:9a2f3e1fab807f87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeInsertSibling(_:_:)

<sub>Function</sub>

Inserts a new sibling after a given tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeInsertSibling(_ tree: CFTree!, _ newSibling: CFTree!)
```

## Parameters

- `tree` — The tree after which to insert `newSibling`. `tree` must have a parent.

- `newSibling` — The sibling to add. `newSibling` must not have a parent.

## Discussion

When a child tree is added to another tree, the child tree is retained by its new parent.

If you want to manipulate an existing tree structure, since `newSibling` must not have a parent you need to remove a tree from its parent in order to move it to a new position. If you do this, you should retain the tree before you actually remove it from its parent (see [CFTreeRemove](<cftreeremove(__).md>)).

## See Also

### Modifying a Tree

- [CFTreeAppendChild](<cftreeappendchild(____).md>) — Adds a new child to a tree as the last in its list of children.
- [CFTreeRemoveAllChildren](<cftreeremoveallchildren(__).md>) — Removes all the children of a tree.
- [CFTreePrependChild](<cftreeprependchild(____).md>) — Adds a new child to the specified tree as the first in its list of children.
- [CFTreeRemove](<cftreeremove(__).md>) — Removes a tree from its parent.
- [CFTreeSetContext](<cftreesetcontext(____).md>) — Replaces the context of a tree by releasing the old information pointer and retaining the new one.

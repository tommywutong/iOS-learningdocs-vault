---
title: 'CFTreeAppendChild(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreeappendchild(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreeappendchild(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreeappendchild%28_%3A_%3A%29.json'
content_hash: 'sha256:361fda9b8601b414'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeAppendChild(_:_:)

<sub>Function</sub>

Adds a new child to a tree as the last in its list of children.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeAppendChild(_ tree: CFTree!, _ newChild: CFTree!)
```

## Parameters

- `tree` — The tree to which to add `newChild`.

- `newChild` — The child tree to add to `tree`. If this parameter is a tree which is already a child of any other tree, the behavior is undefined.

## Discussion

When a child tree is added to another tree, the child tree is retained by its new parent.

## See Also

### Modifying a Tree

- [CFTreeInsertSibling](<cftreeinsertsibling(____).md>) — Inserts a new sibling after a given tree.
- [CFTreeRemoveAllChildren](<cftreeremoveallchildren(__).md>) — Removes all the children of a tree.
- [CFTreePrependChild](<cftreeprependchild(____).md>) — Adds a new child to the specified tree as the first in its list of children.
- [CFTreeRemove](<cftreeremove(__).md>) — Removes a tree from its parent.
- [CFTreeSetContext](<cftreesetcontext(____).md>) — Replaces the context of a tree by releasing the old information pointer and retaining the new one.

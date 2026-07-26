---
title: 'CFTreeSetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreesetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreesetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreesetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:5f114a747623f60a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeSetContext(_:_:)

<sub>Function</sub>

Replaces the context of a tree by releasing the old information pointer and retaining the new one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeSetContext(_ tree: CFTree!, _ context: UnsafePointer<CFTreeContext>!)
```

## Parameters

- `tree` — The tree to modify.

- `context` — The [CFTreeContext](cftreecontext.md) structure to be copied and used as the context of the new tree. The information pointer will be retained by the tree if a retain function is provided. If this value is not a valid C pointer to a [CFTreeContext](cftreecontext.md) structure-sized block of storage, the result is undefined. If the version number of the storage is not a valid [CFTreeContext](cftreecontext.md) version number, the result is undefined.

## See Also

### Modifying a Tree

- [CFTreeAppendChild](<cftreeappendchild(____).md>) — Adds a new child to a tree as the last in its list of children.
- [CFTreeInsertSibling](<cftreeinsertsibling(____).md>) — Inserts a new sibling after a given tree.
- [CFTreeRemoveAllChildren](<cftreeremoveallchildren(__).md>) — Removes all the children of a tree.
- [CFTreePrependChild](<cftreeprependchild(____).md>) — Adds a new child to the specified tree as the first in its list of children.
- [CFTreeRemove](<cftreeremove(__).md>) — Removes a tree from its parent.

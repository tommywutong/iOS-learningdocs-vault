---
title: 'CFTreeRemoveAllChildren(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreeremoveallchildren(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreeremoveallchildren(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreeremoveallchildren%28_%3A%29.json'
content_hash: 'sha256:62a6d83091aadbbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeRemoveAllChildren(_:)

<sub>Function</sub>

Removes all the children of a tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeRemoveAllChildren(_ tree: CFTree!)
```

## Parameters

- `tree` — The tree to modify.

## See Also

### Modifying a Tree

- [CFTreeAppendChild](<cftreeappendchild(____).md>) — Adds a new child to a tree as the last in its list of children.
- [CFTreeInsertSibling](<cftreeinsertsibling(____).md>) — Inserts a new sibling after a given tree.
- [CFTreePrependChild](<cftreeprependchild(____).md>) — Adds a new child to the specified tree as the first in its list of children.
- [CFTreeRemove](<cftreeremove(__).md>) — Removes a tree from its parent.
- [CFTreeSetContext](<cftreesetcontext(____).md>) — Replaces the context of a tree by releasing the old information pointer and retaining the new one.

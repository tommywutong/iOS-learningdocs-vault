---
title: 'CFTreeGetChildren(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreegetchildren(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreegetchildren(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreegetchildren%28_%3A_%3A%29.json'
content_hash: 'sha256:b16e20a6b3241f93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeGetChildren(_:_:)

<sub>Function</sub>

Fills a buffer with children from the tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeGetChildren(_ tree: CFTree!, _ children: UnsafeMutablePointer<Unmanaged<CFTree>?>!)
```

## Parameters

- `tree` — The tree to examine.

- `children` — The C array of pointer-sized values to be filled with the children from `tree`. This value must be a valid pointer to a C array of at least the size of the number of children in `tree`. Use the [CFTreeGetChildCount](<cftreegetchildcount(__).md>) function to obtain the number of children in `tree`. You are responsible for retaining and releasing the returned objects as needed.

## See Also

### Examining a Tree

- [CFTreeFindRoot](<cftreefindroot(__).md>) — Returns the root tree of a given tree.
- [CFTreeGetChildAtIndex](<cftreegetchildatindex(____).md>) — Returns the child of a tree at the specified index.
- [CFTreeGetChildCount](<cftreegetchildcount(__).md>) — Returns the number of children in a tree.
- [CFTreeGetContext](<cftreegetcontext(____).md>) — Returns the context of the specified tree.
- [CFTreeGetFirstChild](<cftreegetfirstchild(__).md>) — Returns the first child of a tree.
- [CFTreeGetNextSibling](<cftreegetnextsibling(__).md>) — Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [CFTreeGetParent](<cftreegetparent(__).md>) — Returns the parent of a given tree.

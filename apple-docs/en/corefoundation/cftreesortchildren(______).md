---
title: 'CFTreeSortChildren(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreesortchildren(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreesortchildren(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreesortchildren%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8ea2c5f29e732d08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeSortChildren(_:_:_:)

<sub>Function</sub>

Sorts the immediate children of a tree using a specified comparator function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CFComparatorFunction!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `tree` — The tree to sort.

- `comparator` — The function with a comparator function type signature which is used in the sort operation to compare children of the tree. The children of the tree are sorted from least to greatest according to this function.

- `context` — A pointer-sized program-defined value that is passed to the comparator function, but is otherwise unused by this function.

## Discussion

Note that the comparator only operates one level deep and does not operate on descendants further removed than the immediate children of a tree node.

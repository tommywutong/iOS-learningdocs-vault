---
title: 'CFTreeApplyFunctionToChildren(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreeapplyfunctiontochildren(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreeapplyfunctiontochildren(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreeapplyfunctiontochildren%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:03e55c9db45a424b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeApplyFunctionToChildren(_:_:_:)

<sub>Function</sub>

Calls a function once for each immediate child of a tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `tree` — The tree to operate upon.

- `applier` — The callback function to call once for each child in `tree`. The function must be able to apply to all the values in the tree.

- `context` — A pointer-sized program-defined value that is passed to the applier function, but is otherwise unused by this function.

## Discussion

Note that the applier only operates one level deep—it does not operate on descendants further removed than the immediate children of a tree. If the tree is mutable, it is unsafe for the applied function to change the contents of the tree.

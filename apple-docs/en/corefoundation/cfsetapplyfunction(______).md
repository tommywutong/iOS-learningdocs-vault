---
title: 'CFSetApplyFunction(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetapplyfunction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetapplyfunction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetapplyfunction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a6bed6b6bcc4c501'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetApplyFunction(_:_:_:)

<sub>Function</sub>

Calls a function once for each value in a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetApplyFunction(_ theSet: CFSet!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `theSet` — The set to operate upon.

- `applier` — The callback function to call once for each value in the `theSet`. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The `applier` function must be able to work with all values in `theSet`.

- `context` — A pointer-sized program-defined value, which is passed as the second parameter to the `applier` function, but is otherwise unused by this function.

## Discussion

If `theSet` is mutable, it is unsafe for the `applier` function to change the contents of the collection.

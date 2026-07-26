---
title: 'CFArrayApplyFunction(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayapplyfunction(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayapplyfunction(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayapplyfunction%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9fbda43d02e978c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayApplyFunction(_:_:_:_:)

<sub>Function</sub>

Calls a function once for each element in range in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `theArray` — The array to whose elements to apply the function.

- `range` — The range of values within `theArray` to which to apply the `applier` function. The range must not exceed the bounds of `theArray`. The range may be empty (length `0`).

- `applier` — The callback function to call once for each value in the given range in `theArray`. If there are values in the range that the `applier` function does not expect or cannot properly apply to, the behavior is undefined.

- `context` — A pointer-sized program-defined value, which is passed as the second argument to the `applier` function, but is otherwise unused by this function. If the context is not what is expected by the applier function, the behavior is undefined.

## Discussion

While this function iterates over a mutable collection, it is unsafe for the `applier` function to change the contents of the collection.

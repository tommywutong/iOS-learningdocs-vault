---
title: 'CFBagApplyFunction(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagapplyfunction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagapplyfunction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagapplyfunction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f8dc69c74a0dab94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagApplyFunction(_:_:_:)

<sub>Function</sub>

Calls a function once for each value in a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagApplyFunction(_ theBag: CFBag!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `theBag` — The bag to operate upon.

- `applier` — The callback function to call once for each value in the `theBag`. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. If there are values in the range that the `applier` function does not expect or cannot properly apply to, the behavior is undefined.

- `context` — A pointer-sized program-defined value, which is passed as the second parameter to the `applier` function, but is otherwise unused by this function. If the context is not what is expected by the applier function, the behavior is undefined.

## Discussion

While this function iterates over a mutable collection, it is unsafe for the `applier` function to change the contents of the collection.

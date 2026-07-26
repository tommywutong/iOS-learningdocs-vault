---
title: 'CFDictionaryApplyFunction(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionaryapplyfunction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryapplyfunction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryapplyfunction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0d935d5fc19180df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryApplyFunction(_:_:_:)

<sub>Function</sub>

Calls a function once for each key-value pair in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `theDict` — The dictionary to operate upon.

- `applier` — The callback function to call once for each key-value pair in `theDict`. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. If there are keys or values which the `applier` function does not expect or cannot properly apply to, the behavior is undefined.

- `context` — A pointer-sized program-defined value, which is passed as the third parameter to the applier function, but is otherwise unused by this function. The value must be appropriate for the `applier` function.

## Discussion

If this function iterates over a mutable collection, it is unsafe for the `applier` function to change the contents of the collection.

---
title: 'merge(_:uniquingKeysWith:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/merge(_:uniquingkeyswith:)-1u8be'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/merge(_:uniquingkeyswith:)-1u8be'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/merge%28_%3Auniquingkeyswith%3A%29-1u8be.json'
content_hash: 'sha256:f73625681401e0a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# merge(_:uniquingKeysWith:)

<sub>Instance Method</sub>

Merges the given dictionary into this dictionary, using a combining closure to determine the value for any duplicate keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func merge<E>(_ other: [Key : Value], uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) where E : Error
```

## Parameters

- `other` — A dictionary to merge.

- `combine` — A closure that takes the current and new values for any duplicate keys. The closure returns the desired value for the final dictionary.

## Discussion

Use the `combine` closure to select a value to use in the updated dictionary, or to combine existing and new values. As the key-values pairs in `other` are merged with this dictionary, the `combine` closure is called with the current and new values for any duplicate keys that are encountered.

This example shows how to choose the current or new values for any duplicate keys:

```swift
var dictionary = ["a": 1, "b": 2]

// Keeping existing value for key "a":
dictionary.merge(["a": 3, "c": 4]) { (current, _) in current }
// ["b": 2, "a": 1, "c": 4]

// Taking the new value for key "a":
dictionary.merge(["a": 5, "d": 6]) { (_, new) in new }
// ["b": 2, "a": 5, "c": 4, "d": 6]
```

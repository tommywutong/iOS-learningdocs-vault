---
title: 'merging(_:uniquingKeysWith:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/merging(_:uniquingkeyswith:)-4vrqz'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/merging(_:uniquingkeyswith:)-4vrqz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/merging%28_%3Auniquingkeyswith%3A%29-4vrqz.json'
content_hash: 'sha256:4693932530752372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# merging(_:uniquingKeysWith:)

<sub>Instance Method</sub>

Creates a dictionary by merging the given dictionary into this dictionary, using a combining closure to determine the value for duplicate keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merging<E>(_ other: [Key : Value], uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) -> [Key : Value] where E : Error
```

## Parameters

- `other` — A dictionary to merge.

- `combine` — A closure that takes the current and new values for any duplicate keys. The closure returns the desired value for the final dictionary.

## Return Value

A new dictionary with the combined keys and values of this dictionary and `other`.

## Discussion

Use the `combine` closure to select a value to use in the returned dictionary, or to combine existing and new values. As the key-value pairs in `other` are merged with this dictionary, the `combine` closure is called with the current and new values for any duplicate keys that are encountered.

This example shows how to choose the current or new values for any duplicate keys:

```swift
let dictionary = ["a": 1, "b": 2]
let otherDictionary = ["a": 3, "b": 4]

let keepingCurrent = dictionary.merging(otherDictionary)
      { (current, _) in current }
// ["b": 2, "a": 1]
let replacingCurrent = dictionary.merging(otherDictionary)
      { (_, new) in new }
// ["b": 4, "a": 3]
```

---
title: 'init(uniqueKeysWithValues:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/init(uniquekeyswithvalues:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/init(uniquekeyswithvalues:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/init%28uniquekeyswithvalues%3A%29.json'
content_hash: 'sha256:b32f49473adc56d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# init(uniqueKeysWithValues:)

<sub>Initializer</sub>

Creates a new dictionary from the key-value pairs in the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(uniqueKeysWithValues keysAndValues: S) where S : Sequence, S.Element == (Key, Value)
```

## Parameters

- `keysAndValues` — A sequence of key-value pairs to use for the new dictionary. Every key in `keysAndValues` must be unique.

## Return Value

A new dictionary initialized with the elements of `keysAndValues`.

## Discussion

You use this initializer to create a dictionary when you have a sequence of key-value tuples with unique keys. Passing a sequence with duplicate keys to this initializer results in a runtime error. If your sequence might have duplicate keys, use the `Dictionary(_:uniquingKeysWith:)` initializer instead.

The following example creates a new dictionary using an array of strings as the keys and the integers in a countable range as the values:

```swift
let digitWords = ["one", "two", "three", "four", "five"]
let wordToValue = Dictionary(uniqueKeysWithValues: zip(digitWords, 1...5))
print(wordToValue["three"]!)
// Prints "3"
print(wordToValue)
// Prints "["three": 3, "four": 4, "five": 5, "one": 1, "two": 2]"
```

> [!info] Precondition
> The sequence must not have duplicate keys.

## See Also

### Creating a Dictionary

- [init()](<init().md>) — Creates an empty dictionary.
- [init(minimumCapacity:)](<init(minimumcapacity_).md>) — Creates an empty dictionary with preallocated space for at least the specified number of elements.
- [init(_:uniquingKeysWith:)](<init(__uniquingkeyswith_).md>) — Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init(grouping:by:)](<init(grouping_by_).md>) — Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.

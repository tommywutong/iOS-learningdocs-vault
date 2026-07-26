---
title: 'init(minimumCapacity:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/init(minimumcapacity:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/init(minimumcapacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/init%28minimumcapacity%3A%29.json'
content_hash: 'sha256:430298859537b794'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# init(minimumCapacity:)

<sub>Initializer</sub>

Creates an empty dictionary with preallocated space for at least the specified number of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(minimumCapacity: Int)
```

## Parameters

- `minimumCapacity` — The minimum number of key-value pairs that the newly created dictionary should be able to store without reallocating its storage buffer.

## Discussion

Use this initializer to avoid intermediate reallocations of a dictionary’s storage buffer when you know how many key-value pairs you are adding to a dictionary after creation.

## See Also

### Creating a Dictionary

- [init()](<init().md>) — Creates an empty dictionary.
- [init(uniqueKeysWithValues:)](<init(uniquekeyswithvalues_).md>) — Creates a new dictionary from the key-value pairs in the given sequence.
- [init(_:uniquingKeysWith:)](<init(__uniquingkeyswith_).md>) — Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init(grouping:by:)](<init(grouping_by_).md>) — Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.

---
title: 'init(grouping:by:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/init(grouping:by:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/init(grouping:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/init%28grouping%3Aby%3A%29.json'
content_hash: 'sha256:ff5142720387acca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# init(grouping:by:)

<sub>Initializer</sub>

Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S, E>(grouping values: S, by keyForValue: (S.Element) throws(E) -> Key) throws(E) where Value == [S.Element], S : Sequence, E : Error
```

## Parameters

- `values` — A sequence of values to group into a dictionary.

- `keyForValue` — A closure that returns a key for each element in `values`.

## Discussion

The arrays in the “values” position of the new dictionary each contain at least one element, with the elements in the same order as the source sequence.

The following example declares an array of names, and then creates a dictionary from that array by grouping the names by first letter:

```swift
let students = ["Kofi", "Abena", "Efua", "Kweku", "Akosua"]
let studentsByLetter = Dictionary(grouping: students, by: { $0.first! })
// ["E": ["Efua"], "K": ["Kofi", "Kweku"], "A": ["Abena", "Akosua"]]
```

The new `studentsByLetter` dictionary has three entries, with students’ names grouped by the keys `"E"`, `"K"`, and `"A"`.

## See Also

### Creating a Dictionary

- [init()](<init().md>) — Creates an empty dictionary.
- [init(minimumCapacity:)](<init(minimumcapacity_).md>) — Creates an empty dictionary with preallocated space for at least the specified number of elements.
- [init(uniqueKeysWithValues:)](<init(uniquekeyswithvalues_).md>) — Creates a new dictionary from the key-value pairs in the given sequence.
- [init(_:uniquingKeysWith:)](<init(__uniquingkeyswith_).md>) — Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.

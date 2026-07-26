---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/init(_:)-9cgks'
source_url: 'https://developer.apple.com/documentation/swift/set/init(_:)-9cgks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/init%28_%3A%29-9cgks.json'
content_hash: 'sha256:1f9049ef9150e1ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# init(_:)

<sub>Initializer</sub>

Creates a new set from a finite sequence of items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

## Parameters

- `sequence` — The elements to use as members of the new set.

## Discussion

Use this initializer to create a new set from an existing sequence, like an array or a range:

```swift
let validIndices = Set(0..<7).subtracting([2, 4, 5])
print(validIndices)
// Prints "[6, 0, 1, 3]"
```

## See Also

### Creating a Set

- [init()](<init().md>) — Creates an empty set.
- [init(minimumCapacity:)](<init(minimumcapacity_).md>) — Creates an empty set with preallocated space for at least the specified number of elements.
- [init(_:)](<init(__).md>) — Creates a new set from a finite sequence of items.

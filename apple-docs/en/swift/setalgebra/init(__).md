---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/init%28_%3A%29.json'
content_hash: 'sha256:9c5df0c68a47efea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

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

## Default Implementations

### SetAlgebra Implementations

- [init(_:)](<init(__)-5ink1.md>) — Creates a new set from a finite sequence of items.

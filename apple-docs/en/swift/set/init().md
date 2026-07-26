---
title: init()
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/init()
source_url: 'https://developer.apple.com/documentation/swift/set/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/init%28%29.json'
content_hash: 'sha256:e3ff98ddf1dad293'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# init()

<sub>Initializer</sub>

Creates an empty set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

This is equivalent to initializing with an empty array literal. For example:

```swift
var emptySet = Set<Int>()
print(emptySet.isEmpty)
// Prints "true"

emptySet = []
print(emptySet.isEmpty)
// Prints "true"
```

## See Also

### Creating a Set

- [init(minimumCapacity:)](<init(minimumcapacity_).md>) — Creates an empty set with preallocated space for at least the specified number of elements.
- [init(_:)](<init(__)-9cgks.md>) — Creates a new set from a finite sequence of items.
- [init(_:)](<init(__).md>) — Creates a new set from a finite sequence of items.

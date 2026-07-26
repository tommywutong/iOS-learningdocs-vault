---
title: init()
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/setalgebra/init()
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/init%28%29.json'
content_hash: 'sha256:bb0d311f47e7985d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# init()

<sub>Initializer</sub>

Creates an empty set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

This initializer is equivalent to initializing with an empty array literal. For example, you create an empty `Set` instance with either this initializer or with an empty array literal.

```swift
var emptySet = Set<Int>()
print(emptySet.isEmpty)
// Prints "true"

emptySet = []
print(emptySet.isEmpty)
// Prints "true"
```

## Default Implementations

### SetAlgebra Implementations

- [init()](<init()-3obov.md>) — Creates an empty option set.

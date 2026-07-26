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
doc_path: /documentation/swift/contiguousarray/init()
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/init%28%29.json'
content_hash: 'sha256:256c5fb915fc3200'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# init()

<sub>Initializer</sub>

Creates a new, empty array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

This is equivalent to initializing with an empty array literal. For example:

```swift
var emptyArray = Array<Int>()
print(emptyArray.isEmpty)
// Prints "true"

emptyArray = []
print(emptyArray.isEmpty)
// Prints "true"
```

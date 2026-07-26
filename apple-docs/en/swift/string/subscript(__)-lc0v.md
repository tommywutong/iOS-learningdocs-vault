---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/subscript(_:)-lc0v'
source_url: 'https://developer.apple.com/documentation/swift/string/subscript(_:)-lc0v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/subscript%28_%3A%29-lc0v.json'
content_hash: 'sha256:dbdd930ee0660a58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the character at the given position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: String.Index) -> Character { get }
```

## Parameters

- `i` — A valid index of the string. `i` must be less than the string’s end index.

## Overview

You can use the same indices for subscripting a string and its substring. For example, this code finds the first letter after the first space:

```swift
let str = "Greetings, friend! How are you?"
let firstSpace = str.firstIndex(of: " ") ?? str.endIndex
let substr = str[firstSpace...]
if let nextCapital = substr.firstIndex(where: { $0 >= "A" && $0 <= "Z" }) {
    print("Capital after a space: \(str[nextCapital])")
}
// Prints "Capital after a space: H"
```

## See Also

### Getting Characters and Bytes

- [first](first.md) — The first element of the collection.
- [last](last.md) — The last element of the collection.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.

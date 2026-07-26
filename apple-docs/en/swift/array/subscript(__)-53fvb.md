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
doc_path: '/documentation/swift/array/subscript(_:)-53fvb'
source_url: 'https://developer.apple.com/documentation/swift/array/subscript(_:)-53fvb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/subscript%28_%3A%29-53fvb.json'
content_hash: 'sha256:eb01447e01446cff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses a contiguous subrange of the array’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: Range<Int>) -> ArraySlice<Element> { get set }
```

## Parameters

- `bounds` — A range of integers. The bounds of the range must be valid indices of the array.

## Overview

The returned `ArraySlice` instance uses the same indices for the same elements as the original array. In particular, that slice, unlike an array, may have a nonzero `startIndex` and an `endIndex` that is not equal to `count`. Always use the slice’s `startIndex` and `endIndex` properties instead of assuming that its indices start or end at a particular value.

This example demonstrates getting a slice of an array of strings, finding the index of one of the strings in the slice, and then using that index in the original array.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2 ..< streets.endIndex]
print(streetsSlice)
// Prints "["Channing", "Douglas", "Evarts"]"

let i = streetsSlice.firstIndex(of: "Evarts")    // 4
print(streets[i!])
// Prints "Evarts"
```

## See Also

### Accessing Elements

- [subscript(_:)](<subscript(__)-25iat.md>) — Accesses the element at the specified position.
- [first](first.md) — The first element of the collection.
- [last](last.md) — The last element of the collection.
- [subscript(_:)](<subscript(__)-3kwny.md>)
- [subscript(_:)](<subscript(__)-4h7rl.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-3pmfg.md>)
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.

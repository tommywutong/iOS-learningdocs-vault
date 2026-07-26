---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablecollection/subscript(_:)-31dgt'
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/subscript(_:)-31dgt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/subscript%28_%3A%29-31dgt.json'
content_hash: 'sha256:cb778ccfe8427ed3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses a contiguous subrange of the collection’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override subscript(bounds: Range<Self.Index>) -> Self.SubSequence { get set }
```

## Parameters

- `bounds` — A range of the collection’s indices. The bounds of the range must be valid indices of the collection.

## Overview

The accessed slice uses the same indices for the same elements as the original collection. Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value.

This example demonstrates getting a slice of an array of strings, finding the index of one of the strings in the slice, and then using that index in the original array.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2 ..< streets.endIndex]
print(streetsSlice)
// Prints "["Channing", "Douglas", "Evarts"]"

let index = streetsSlice.firstIndex(of: "Evarts")    // 4
streets[index!] = "Eustace"
print(streets[index!])
// Prints "Eustace"
```

> [!abstract] Complexity
> O(1)

## Default Implementations

### MutableCollection Implementations

- [subscript(_:)](<subscript(__)-1wd4v.md>)
- [subscript(_:)](<subscript(__)-2qem1.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-37d4d.md>)

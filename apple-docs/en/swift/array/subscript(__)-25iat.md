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
doc_path: '/documentation/swift/array/subscript(_:)-25iat'
source_url: 'https://developer.apple.com/documentation/swift/array/subscript(_:)-25iat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/subscript%28_%3A%29-25iat.json'
content_hash: 'sha256:5fd25e3db9566129'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> Element { get set }
```

## Parameters

- `index` — The position of the element to access. `index` must be greater than or equal to `startIndex` and less than `endIndex`.

## Overview

The following example uses indexed subscripting to update an array’s second element. After assigning the new value (`"Butler"`) at a specific position, that value is immediately available at that same position.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets[1] = "Butler"
print(streets[1])
// Prints "Butler"
```

> [!abstract] Complexity
> Reading an element from an array is O(1). Writing is O(1) unless the array’s storage is shared with another array or uses a bridged `NSArray` instance as its storage, in which case writing is O(_n_), where _n_ is the length of the array.

## See Also

### Accessing Elements

- [first](first.md) — The first element of the collection.
- [last](last.md) — The last element of the collection.
- [subscript(_:)](<subscript(__)-53fvb.md>) — Accesses a contiguous subrange of the array’s elements.
- [subscript(_:)](<subscript(__)-3kwny.md>)
- [subscript(_:)](<subscript(__)-4h7rl.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-3pmfg.md>)
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.

---
title: 'subtracting(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/subtracting(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/subtracting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/subtracting%28_%3A%29.json'
content_hash: 'sha256:33c21e0277f09278'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# subtracting(_:)

<sub>Instance Method</sub>

Returns a new set containing the elements of this set that do not occur in the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subtracting(_ other: Self) -> Self
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

A new set.

## Discussion

In the following example, the `nonNeighbors` set is made up of the elements of the `employees` set that are not elements of `neighbors`:

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
let nonNeighbors = employees.subtracting(neighbors)
print(nonNeighbors)
// Prints "["Diana", "Chris", "Alicia"]"
```

## Default Implementations

### SetAlgebra Implementations

- [subtracting(_:)](<subtracting(__)-648yh.md>) — Returns a new set containing the elements of this set that do not occur in the given set.

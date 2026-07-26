---
title: 'symmetricDifference(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/symmetricdifference(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/symmetricdifference(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/symmetricdifference%28_%3A%29.json'
content_hash: 'sha256:c6afee649a5d7f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# symmetricDifference(_:)

<sub>Instance Method</sub>

Returns a new set with the elements that are either in this set or in the given set, but not in both.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func symmetricDifference(_ other: Self) -> Self
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

A new set.

## Discussion

In the following example, the `eitherNeighborsOrEmployees` set is made up of the elements of the `employees` and `neighbors` sets that are not in both `employees` _and_ `neighbors`. In particular, the names `"Bethany"` and `"Eric"` do not appear in `eitherNeighborsOrEmployees`.

```swift
let employees: Set = ["Alicia", "Bethany", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani"]
let eitherNeighborsOrEmployees = employees.symmetricDifference(neighbors)
print(eitherNeighborsOrEmployees)
// Prints "["Diana", "Forlani", "Alicia"]"
```

## Default Implementations

### SetAlgebra Implementations

- [symmetricDifference(_:)](<symmetricdifference(__)-81pzi.md>) — Returns a new option set with the elements contained in this set or in the given set, but not in both.

## See Also

### Combining Sets

- [union(_:)](<union(__).md>) — Returns a new set with the elements of both this and the given set.
- [formUnion(_:)](<formunion(__).md>) — Adds the elements of the given set to the set.
- [intersection(_:)](<intersection(__).md>) — Returns a new set with the elements that are common to both this set and the given set.
- [formIntersection(_:)](<formintersection(__).md>) — Removes the elements of this set that aren’t also in the given set.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__).md>) — Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.

---
title: 'intersection(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/intersection(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/intersection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/intersection%28_%3A%29.json'
content_hash: 'sha256:68425151110534b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# intersection(_:)

<sub>Instance Method</sub>

Returns a new set with the elements that are common to both this set and the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersection(_ other: Self) -> Self
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

A new set.

## Discussion

In the following example, the `bothNeighborsAndEmployees` set is made up of the elements that are in _both_ the `employees` and `neighbors` sets. Elements that are in only one or the other are left out of the result of the intersection.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
let bothNeighborsAndEmployees = employees.intersection(neighbors)
print(bothNeighborsAndEmployees)
// Prints "["Bethany", "Eric"]"
```

> [!note] Note
> If this set and `other` contain elements that are equal but distinguishable (e.g. via `===`), which of these elements is present in the result is unspecified.

## Default Implementations

### SetAlgebra Implementations

- [intersection(_:)](<intersection(__)-73uhs.md>) — Returns a new option set with only the elements contained in both this set and the given set.

## See Also

### Combining Sets

- [union(_:)](<union(__).md>) — Returns a new set with the elements of both this and the given set.
- [formUnion(_:)](<formunion(__).md>) — Adds the elements of the given set to the set.
- [formIntersection(_:)](<formintersection(__).md>) — Removes the elements of this set that aren’t also in the given set.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__).md>) — Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.

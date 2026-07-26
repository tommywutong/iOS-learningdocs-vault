---
title: 'union(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/union(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/union(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/union%28_%3A%29.json'
content_hash: 'sha256:103164748a561549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# union(_:)

<sub>Instance Method</sub>

Returns a new set with the elements of both this and the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func union(_ other: Self) -> Self
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

A new set with the unique elements of this set and `other`.

## Discussion

In the following example, the `attendeesAndVisitors` set is made up of the elements of the `attendees` and `visitors` sets:

```swift
let attendees: Set = ["Alicia", "Bethany", "Diana"]
let visitors = ["Marcia", "Nathaniel"]
let attendeesAndVisitors = attendees.union(visitors)
print(attendeesAndVisitors)
// Prints "["Diana", "Nathaniel", "Bethany", "Alicia", "Marcia"]"
```

If the set already contains one or more elements that are also in `other`, the existing members are kept.

```swift
let initialIndices = Set(0..<5)
let expandedIndices = initialIndices.union([2, 3, 6, 7])
print(expandedIndices)
// Prints "[2, 4, 6, 7, 0, 1, 3]"
```

> [!note] Note
> If this set and `other` contain elements that are equal but distinguishable (e.g. via `===`), which of these elements is present in the result is unspecified.

## Default Implementations

### SetAlgebra Implementations

- [union(_:)](<union(__)-7mfo6.md>) — Returns a new option set of the elements contained in this set, in the given set, or in both.

## See Also

### Combining Sets

- [formUnion(_:)](<formunion(__).md>) — Adds the elements of the given set to the set.
- [intersection(_:)](<intersection(__).md>) — Returns a new set with the elements that are common to both this set and the given set.
- [formIntersection(_:)](<formintersection(__).md>) — Removes the elements of this set that aren’t also in the given set.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__).md>) — Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.

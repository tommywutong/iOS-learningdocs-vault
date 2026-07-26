---
title: 'formUnion(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/formunion(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/formunion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/formunion%28_%3A%29.json'
content_hash: 'sha256:fb578f4ff9aca382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# formUnion(_:)

<sub>Instance Method</sub>

Adds the elements of the given set to the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formUnion(_ other: Self)
```

## Parameters

- `other` — A set of the same type as the current set.

## Discussion

In the following example, the elements of the `visitors` set are added to the `attendees` set:

```swift
var attendees: Set = ["Alicia", "Bethany", "Diana"]
let visitors: Set = ["Diana", "Marcia", "Nathaniel"]
attendees.formUnion(visitors)
print(attendees)
// Prints "["Diana", "Nathaniel", "Bethany", "Alicia", "Marcia"]"
```

If the set already contains one or more elements that are also in `other`, the existing members are kept.

```swift
var initialIndices = Set(0..<5)
initialIndices.formUnion([2, 3, 6, 7])
print(initialIndices)
// Prints "[2, 4, 6, 7, 0, 1, 3]"
```

## Default Implementations

### SetAlgebra Implementations

- [formUnion(_:)](<formunion(__)-4ht9l.md>) — Inserts the elements of another set into this option set.

## See Also

### Combining Sets

- [union(_:)](<union(__).md>) — Returns a new set with the elements of both this and the given set.
- [intersection(_:)](<intersection(__).md>) — Returns a new set with the elements that are common to both this set and the given set.
- [formIntersection(_:)](<formintersection(__).md>) — Removes the elements of this set that aren’t also in the given set.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__).md>) — Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.

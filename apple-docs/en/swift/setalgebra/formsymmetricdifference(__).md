---
title: 'formSymmetricDifference(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/formsymmetricdifference(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/formsymmetricdifference(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/formsymmetricdifference%28_%3A%29.json'
content_hash: 'sha256:a09b9642ee91f4e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# formSymmetricDifference(_:)

<sub>Instance Method</sub>

Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formSymmetricDifference(_ other: Self)
```

## Parameters

- `other` — A set of the same type.

## Discussion

In the following example, the elements of the `employees` set that are also members of `neighbors` are removed from `employees`, while the elements of `neighbors` that are not members of `employees` are added to `employees`. In particular, the names `"Bethany"` and `"Eric"` are removed from `employees` while the name `"Forlani"` is added.

```swift
var employees: Set = ["Alicia", "Bethany", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani"]
employees.formSymmetricDifference(neighbors)
print(employees)
// Prints "["Diana", "Forlani", "Alicia"]"
```

## Default Implementations

### SetAlgebra Implementations

- [formSymmetricDifference(_:)](<formsymmetricdifference(__)-56m23.md>) — Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.

## See Also

### Combining Sets

- [union(_:)](<union(__).md>) — Returns a new set with the elements of both this and the given set.
- [formUnion(_:)](<formunion(__).md>) — Adds the elements of the given set to the set.
- [intersection(_:)](<intersection(__).md>) — Returns a new set with the elements that are common to both this set and the given set.
- [formIntersection(_:)](<formintersection(__).md>) — Removes the elements of this set that aren’t also in the given set.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given set, but not in both.

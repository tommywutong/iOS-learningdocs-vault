---
title: 'formIntersection(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/formintersection(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/formintersection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/formintersection%28_%3A%29.json'
content_hash: 'sha256:731153d39be82db1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# formIntersection(_:)

<sub>Instance Method</sub>

Removes the elements of this set that aren’t also in the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formIntersection(_ other: Self)
```

## Parameters

- `other` — A set of the same type as the current set.

## Discussion

In the following example, the elements of the `employees` set that are not also members of the `neighbors` set are removed. In particular, the names `"Alicia"`, `"Chris"`, and `"Diana"` are removed.

```swift
var employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
employees.formIntersection(neighbors)
print(employees)
// Prints "["Bethany", "Eric"]"
```

## Default Implementations

### SetAlgebra Implementations

- [formIntersection(_:)](<formintersection(__)-9h7lm.md>) — Removes all elements of this option set that are not also present in the given set.

## See Also

### Combining Sets

- [union(_:)](<union(__).md>) — Returns a new set with the elements of both this and the given set.
- [formUnion(_:)](<formunion(__).md>) — Adds the elements of the given set to the set.
- [intersection(_:)](<intersection(__).md>) — Returns a new set with the elements that are common to both this set and the given set.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__).md>) — Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.

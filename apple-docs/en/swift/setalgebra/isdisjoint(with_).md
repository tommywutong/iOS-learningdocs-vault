---
title: 'isDisjoint(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/isdisjoint(with:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/isdisjoint(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/isdisjoint%28with%3A%29.json'
content_hash: 'sha256:51a327d73bacccd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# isDisjoint(with:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the set has no members in common with the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDisjoint(with other: Self) -> Bool
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

`true` if the set has no elements in common with `other`; otherwise, `false`.

## Discussion

In the following example, the `employees` set is disjoint with the `visitors` set because no name appears in both sets.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let visitors: Set = ["Marcia", "Nathaniel", "Olivia"]
print(employees.isDisjoint(with: visitors))
// Prints "true"
```

## Default Implementations

### SetAlgebra Implementations

- [isDisjoint(with:)](<isdisjoint(with_)-59c10.md>) — Returns a Boolean value that indicates whether the set has no members in common with the given set.

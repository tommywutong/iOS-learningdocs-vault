---
title: 'isDisjoint(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/isdisjoint(with:)-8ngmk'
source_url: 'https://developer.apple.com/documentation/swift/set/isdisjoint(with:)-8ngmk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/isdisjoint%28with%3A%29-8ngmk.json'
content_hash: 'sha256:50e0b61f3fb14836'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# isDisjoint(with:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether this set has no members in common with the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDisjoint(with other: Set<Element>) -> Bool
```

## Parameters

- `other` — Another set.

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

## See Also

### Comparing Sets

- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two sets have equal elements.
- [!=(_:_:)](<!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [isSubset(of:)](<issubset(of_)-1d7pp.md>) — Returns a Boolean value that indicates whether this set is a subset of the given set.
- [isSubset(of:)](<issubset(of_)-6qyo5.md>) — Returns a Boolean value that indicates whether the set is a subset of the given sequence.
- [isStrictSubset(of:)](<isstrictsubset(of_)-96vc3.md>) — Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [isStrictSubset(of:)](<isstrictsubset(of_)-787sx.md>) — Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [isSuperset(of:)](<issuperset(of_)-9iz62.md>) — Returns a Boolean value that indicates whether this set is a superset of the given set.
- [isSuperset(of:)](<issuperset(of_)-90hri.md>) — Returns a Boolean value that indicates whether the set is a superset of the given sequence.
- [isStrictSuperset(of:)](<isstrictsuperset(of_)-4d27m.md>) — Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [isStrictSuperset(of:)](<isstrictsuperset(of_)-58ejg.md>) — Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [isDisjoint(with:)](<isdisjoint(with_)-2onid.md>) — Returns a Boolean value that indicates whether the set has no members in common with the given sequence.

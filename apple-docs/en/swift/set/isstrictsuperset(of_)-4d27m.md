---
title: 'isStrictSuperset(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/isstrictsuperset(of:)-4d27m'
source_url: 'https://developer.apple.com/documentation/swift/set/isstrictsuperset(of:)-4d27m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/isstrictsuperset%28of%3A%29-4d27m.json'
content_hash: 'sha256:39e6a95a718eba53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# isStrictSuperset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isStrictSuperset(of other: Set<Element>) -> Bool
```

## Parameters

- `other` — Another set.

## Return Value

`true` if the set is a strict superset of `other`; otherwise, `false`.

## Discussion

Set _A_ is a strict superset of another set _B_ if every member of _B_ is also a member of _A_ and _A_ contains at least one element that is _not_ a member of _B_.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(employees.isStrictSuperset(of: attendees))
// Prints "true"
print(employees.isStrictSuperset(of: employees))
// Prints "false"
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
- [isStrictSuperset(of:)](<isstrictsuperset(of_)-58ejg.md>) — Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [isDisjoint(with:)](<isdisjoint(with_)-8ngmk.md>) — Returns a Boolean value that indicates whether this set has no members in common with the given set.
- [isDisjoint(with:)](<isdisjoint(with_)-2onid.md>) — Returns a Boolean value that indicates whether the set has no members in common with the given sequence.

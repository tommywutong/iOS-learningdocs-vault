---
title: 'isStrictSubset(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/isstrictsubset(of:)-96vc3'
source_url: 'https://developer.apple.com/documentation/swift/set/isstrictsubset(of:)-96vc3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/isstrictsubset%28of%3A%29-96vc3.json'
content_hash: 'sha256:758b5220e6801c18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# isStrictSubset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isStrictSubset(of other: Set<Element>) -> Bool
```

## Parameters

- `other` — Another set.

## Return Value

`true` if the set is a strict subset of `other`; otherwise, `false`.

## Discussion

Set _A_ is a strict subset of another set _B_ if every member of _A_ is also a member of _B_ and _B_ contains at least one element that is not a member of _A_.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(attendees.isStrictSubset(of: employees))
// Prints "true"

// A set is never a strict subset of itself:
print(attendees.isStrictSubset(of: attendees))
// Prints "false"
```

## See Also

### Comparing Sets

- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two sets have equal elements.
- [!=(_:_:)](<!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [isSubset(of:)](<issubset(of_)-1d7pp.md>) — Returns a Boolean value that indicates whether this set is a subset of the given set.
- [isSubset(of:)](<issubset(of_)-6qyo5.md>) — Returns a Boolean value that indicates whether the set is a subset of the given sequence.
- [isStrictSubset(of:)](<isstrictsubset(of_)-787sx.md>) — Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [isSuperset(of:)](<issuperset(of_)-9iz62.md>) — Returns a Boolean value that indicates whether this set is a superset of the given set.
- [isSuperset(of:)](<issuperset(of_)-90hri.md>) — Returns a Boolean value that indicates whether the set is a superset of the given sequence.
- [isStrictSuperset(of:)](<isstrictsuperset(of_)-4d27m.md>) — Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [isStrictSuperset(of:)](<isstrictsuperset(of_)-58ejg.md>) — Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [isDisjoint(with:)](<isdisjoint(with_)-8ngmk.md>) — Returns a Boolean value that indicates whether this set has no members in common with the given set.
- [isDisjoint(with:)](<isdisjoint(with_)-2onid.md>) — Returns a Boolean value that indicates whether the set has no members in common with the given sequence.

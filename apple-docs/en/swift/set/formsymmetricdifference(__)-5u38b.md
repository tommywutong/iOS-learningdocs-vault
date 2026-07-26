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
doc_path: '/documentation/swift/set/formsymmetricdifference(_:)-5u38b'
source_url: 'https://developer.apple.com/documentation/swift/set/formsymmetricdifference(_:)-5u38b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/formsymmetricdifference%28_%3A%29-5u38b.json'
content_hash: 'sha256:94f4a426632adc4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# formSymmetricDifference(_:)

<sub>Instance Method</sub>

Replace this set with the elements contained in this set or the given set, but not both.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formSymmetricDifference<S>(_ other: S) where Element == S.Element, S : Sequence
```

## Parameters

- `other` — A sequence of elements. `other` must be finite.

## Discussion

In the following example, the elements of the `employees` set that are also members of `neighbors` are removed from `employees`, while the elements of `neighbors` that are not members of `employees` are added to `employees`. In particular, the names `"Bethany"` and `"Eric"` are removed from `employees` while the name `"Forlani"` is added.

```swift
var employees: Set = ["Alicia", "Bethany", "Diana", "Eric"]
let neighbors = ["Bethany", "Eric", "Forlani"]
employees.formSymmetricDifference(neighbors)
print(employees)
// Prints "["Diana", "Forlani", "Alicia"]"
```

## See Also

### Combining Sets

- [union(_:)](<union(__).md>) — Returns a new set with the elements of both this set and the given sequence.
- [formUnion(_:)](<formunion(__).md>) — Inserts the elements of the given sequence into the set.
- [intersection(_:)](<intersection(__)-1zh8f.md>) — Returns a new set with the elements that are common to both this set and the given sequence.
- [intersection(_:)](<intersection(__)-6uts9.md>) — Returns a new set with the elements that are common to both this set and the given sequence.
- [formIntersection(_:)](<formintersection(__).md>) — Removes the elements of the set that aren’t also in the given sequence.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given sequence, but not in both.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__)-22p0m.md>) — Removes the elements of the set that are also in the given sequence and adds the members of the sequence that are not already in the set.
- [subtract(_:)](<subtract(__)-8gc48.md>) — Removes the elements of the given set from this set.
- [subtract(_:)](<subtract(__)-7cd3y.md>) — Removes the elements of the given sequence from the set.
- [subtracting(_:)](<subtracting(__)-3n4lc.md>) — Returns a new set containing the elements of this set that do not occur in the given set.
- [subtracting(_:)](<subtracting(__)-2qge3.md>) — Returns a new set containing the elements of this set that do not occur in the given sequence.

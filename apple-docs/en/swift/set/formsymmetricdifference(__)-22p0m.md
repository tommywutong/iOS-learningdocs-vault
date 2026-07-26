---
title: 'formSymmetricDifference(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/formsymmetricdifference(_:)-22p0m'
source_url: 'https://developer.apple.com/documentation/swift/set/formsymmetricdifference(_:)-22p0m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/formsymmetricdifference%28_%3A%29-22p0m.json'
content_hash: 'sha256:521cfce302e85b52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# formSymmetricDifference(_:)

<sub>Instance Method</sub>

Removes the elements of the set that are also in the given sequence and adds the members of the sequence that are not already in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formSymmetricDifference(_ other: Set<Element>)
```

## Parameters

- `other` — Another set.

## Discussion

In the following example, the elements of the `employees` set that are also members of `neighbors` are removed from `employees`, while the elements of `neighbors` that are not members of `employees` are added to `employees`. In particular, the names `"Alicia"`, `"Chris"`, and `"Diana"` are removed from `employees` while the names `"Forlani"` and `"Greta"` are added.

```swift
var employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
employees.formSymmetricDifference(neighbors)
print(employees)
// Prints "["Diana", "Chris", "Forlani", "Alicia", "Greta"]"
```

## See Also

### Combining Sets

- [union(_:)](<union(__).md>) — Returns a new set with the elements of both this set and the given sequence.
- [formUnion(_:)](<formunion(__).md>) — Inserts the elements of the given sequence into the set.
- [intersection(_:)](<intersection(__)-1zh8f.md>) — Returns a new set with the elements that are common to both this set and the given sequence.
- [intersection(_:)](<intersection(__)-6uts9.md>) — Returns a new set with the elements that are common to both this set and the given sequence.
- [formIntersection(_:)](<formintersection(__).md>) — Removes the elements of the set that aren’t also in the given sequence.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given sequence, but not in both.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__)-5u38b.md>) — Replace this set with the elements contained in this set or the given set, but not both.
- [subtract(_:)](<subtract(__)-8gc48.md>) — Removes the elements of the given set from this set.
- [subtract(_:)](<subtract(__)-7cd3y.md>) — Removes the elements of the given sequence from the set.
- [subtracting(_:)](<subtracting(__)-3n4lc.md>) — Returns a new set containing the elements of this set that do not occur in the given set.
- [subtracting(_:)](<subtracting(__)-2qge3.md>) — Returns a new set containing the elements of this set that do not occur in the given sequence.

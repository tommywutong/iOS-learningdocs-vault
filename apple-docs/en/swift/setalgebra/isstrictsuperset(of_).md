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
doc_path: '/documentation/swift/setalgebra/isstrictsuperset(of:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/isstrictsuperset(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/isstrictsuperset%28of%3A%29.json'
content_hash: 'sha256:847da2b241d1d909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# isStrictSuperset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether this set is a strict superset of the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isStrictSuperset(of other: Self) -> Bool
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

`true` if the set is a strict superset of `other`; otherwise, `false`.

## Discussion

Set _A_ is a strict superset of another set _B_ if every member of _B_ is also a member of _A_ and _A_ contains at least one element that is _not_ a member of _B_.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(employees.isStrictSuperset(of: attendees))
// Prints "true"

// A set is never a strict superset of itself:
print(employees.isStrictSuperset(of: employees))
// Prints "false"
```

## See Also

### Comparing Sets

- [isStrictSubset(of:)](<isstrictsubset(of_).md>) — Returns a Boolean value that indicates whether this set is a strict subset of the given set.

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
doc_path: '/documentation/swift/setalgebra/isstrictsubset(of:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/isstrictsubset(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/isstrictsubset%28of%3A%29.json'
content_hash: 'sha256:f18518e0dffc8d4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# isStrictSubset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether this set is a strict subset of the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isStrictSubset(of other: Self) -> Bool
```

## Parameters

- `other` — A set of the same type as the current set.

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

- [isStrictSuperset(of:)](<isstrictsuperset(of_).md>) — Returns a Boolean value that indicates whether this set is a strict superset of the given set.

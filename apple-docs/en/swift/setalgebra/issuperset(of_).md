---
title: 'isSuperset(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/issuperset(of:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/issuperset(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/issuperset%28of%3A%29.json'
content_hash: 'sha256:fc587e6229d4dbc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# isSuperset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the set is a superset of the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isSuperset(of other: Self) -> Bool
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

`true` if the set is a superset of `possibleSubset`; otherwise, `false`.

## Discussion

Set _A_ is a superset of another set _B_ if every member of _B_ is also a member of _A_.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(employees.isSuperset(of: attendees))
// Prints "true"
```

## Default Implementations

### SetAlgebra Implementations

- [isSuperset(of:)](<issuperset(of_)-88ovx.md>) — Returns a Boolean value that indicates whether the set is a superset of the given set.

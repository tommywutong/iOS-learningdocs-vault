---
title: 'isSubset(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/issubset(of:)-5y3lj'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/issubset(of:)-5y3lj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/issubset%28of%3A%29-5y3lj.json'
content_hash: 'sha256:9d3fbc93ef5e6458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# isSubset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the set is a subset of another set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isSubset(of other: Self) -> Bool
```

## Parameters

- `other` — A set of the same type as the current set.

## Return Value

`true` if the set is a subset of `other`; otherwise, `false`.

## Discussion

Set _A_ is a subset of another set _B_ if every member of _A_ is also a member of _B_.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(attendees.isSubset(of: employees))
// Prints "true"
```

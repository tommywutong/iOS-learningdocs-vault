---
title: 'subtract(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/subtract(_:)-7uaak'
source_url: 'https://developer.apple.com/documentation/swift/set/subtract(_:)-7uaak'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/subtract%28_%3A%29-7uaak.json'
content_hash: 'sha256:14ca0c370218d0be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# subtract(_:)

<sub>Instance Method</sub>

Removes the elements of the given set from this set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func subtract(_ other: Self)
```

## Parameters

- `other` — A set of the same type as the current set.

## Discussion

In the following example, the elements of the `employees` set that are also members of the `neighbors` set are removed. In particular, the names `"Bethany"` and `"Eric"` are removed from `employees`.

```swift
var employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
employees.subtract(neighbors)
print(employees)
// Prints "["Diana", "Chris", "Alicia"]"
```

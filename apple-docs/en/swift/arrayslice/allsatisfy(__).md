---
title: 'allSatisfy(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/allsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/allsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/allsatisfy%28_%3A%29.json'
content_hash: 'sha256:529cd592a7705a01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# allSatisfy(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allSatisfy(_ predicate: (Self.Element) throws -> Bool) rethrows -> Bool
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns a Boolean value that indicates whether the passed element satisfies a condition.

## Return Value

`true` if the sequence contains only elements that satisfy `predicate`; otherwise, `false`.

## Discussion

The following code uses this method to test whether all the names in an array have at least five characters:

```swift
let names = ["Sofia", "Camilla", "Martina", "Mateo", "Nicolás"]
let allHaveAtLeastFive = names.allSatisfy({ $0.count >= 5 })
// allHaveAtLeastFive == true
```

If the sequence is empty, this method returns `true`.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.

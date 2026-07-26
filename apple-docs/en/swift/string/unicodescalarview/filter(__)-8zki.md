---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 4.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/unicodescalarview/filter(_:)-8zki'
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/filter(_:)-8zki'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/filter%28_%3A%29-8zki.json'
content_hash: 'sha256:b14d6c5660ba5108'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# filter(_:)

<sub>Instance Method</sub>

Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func filter<E>(_ isIncluded: (Self.Element) throws(E) -> Bool) throws(E) -> Self where E : Error
```

## Parameters

- `isIncluded` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element should be included in the returned collection.

## Return Value

A collection of the elements that `isIncluded` allowed.

## Discussion

In this example, `filter(_:)` is used to include only names shorter than five characters.

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let shortNames = cast.filter { $0.count < 5 }
print(shortNames)
// Prints "["Kim", "Karl"]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

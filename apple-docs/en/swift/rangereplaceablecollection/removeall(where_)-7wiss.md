---
title: 'removeAll(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/removeall(where:)-7wiss'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/removeall(where:)-7wiss'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/removeall%28where%3A%29-7wiss.json'
content_hash: 'sha256:41c9c8bb6390fc18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# removeAll(where:)

<sub>Instance Method</sub>

Removes all the elements that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeAll(where shouldBeRemoved: (Self.Element) throws -> Bool) rethrows
```

## Parameters

- `shouldBeRemoved` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element should be removed from the collection.

## Discussion

Use this method to remove every element in a collection that meets particular criteria. The order of the remaining elements is preserved. This example removes all the odd values from an array of numbers:

```swift
var numbers = [5, 6, 7, 8, 9, 10, 11]
numbers.removeAll(where: { $0 % 2 != 0 })
// numbers == [6, 8, 10]
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

---
title: 'count(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/discontiguousslice/count(where:)'
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice/count(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice/count%28where%3A%29.json'
content_hash: 'sha256:2caa1d97d357f4c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscontiguousSlice](../discontiguousslice.md)

# count(where:)

<sub>Instance Method</sub>

Returns the number of elements in the sequence that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func count<E>(where predicate: (Self.Element) throws(E) -> Bool) throws(E) -> Int where E : Error
```

## Parameters

- `predicate` — A closure that takes each element of the sequence as its argument and returns a Boolean value indicating whether the element should be included in the count.

## Return Value

The number of elements in the sequence that satisfy the given predicate.

## Discussion

You can use this method to count the number of elements that pass a test. The following example finds the number of names that are fewer than five characters long:

```swift
let names = ["Jacqueline", "Ian", "Amy", "Juan", "Soroush", "Tiffany"]
let shortNameCount = names.count(where: { $0.count < 5 })
// shortNameCount == 3
```

To find the number of times a specific element appears in the sequence, use the equal to operator (`==`) in the closure to test for a match.

```swift
let birds = ["duck", "duck", "duck", "duck", "goose"]
let duckCount = birds.count(where: { $0 == "duck" })
// duckCount == 4
```

The sequence must be finite.

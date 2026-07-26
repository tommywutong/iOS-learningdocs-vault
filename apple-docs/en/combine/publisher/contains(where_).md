---
title: 'contains(where:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/contains(where:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/contains(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/contains%28where%3A%29.json'
content_hash: 'sha256:5456f01160508762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# contains(where:)

<sub>Instance Method</sub>

Publishes a Boolean value upon receiving an element that satisfies the predicate closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(where predicate: @escaping (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>
```

## Parameters

- `predicate` — A closure that takes an element as its parameter and returns a Boolean value that indicates whether the element satisfies the closure’s comparison logic.

## Return Value

A publisher that emits the Boolean value `true` when the upstream  publisher emits a matching value.

## Discussion

Use [contains(where:)](<contains(where_).md>) to find the first element in an upstream that satisfies the closure you provide. This operator consumes elements produced from the upstream publisher until the upstream publisher produces a matching element.

This operator is useful when the upstream publisher produces elements that don’t conform to `Equatable`.

In the example below, the [contains(where:)](<contains(where_).md>) operator tests elements against the supplied closure and emits `true` for the first elements that’s greater than `4`, and then finishes normally.

```swift
let numbers = [-1, 0, 10, 5]
numbers.publisher
    .contains {$0 > 4}
    .sink { print("\($0)") }

// Prints: "true"
```

## See Also

### Applying matching criteria to elements

- [contains(_:)](<contains(__).md>) — Publishes a Boolean value upon receiving an element equal to the argument.
- [tryContains(where:)](<trycontains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [tryAllSatisfy(_:)](<tryallsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

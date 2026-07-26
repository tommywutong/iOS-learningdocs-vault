---
title: 'allSatisfy(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/allsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/allsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/allsatisfy%28_%3A%29.json'
content_hash: 'sha256:5b4e7d121290cd0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# allSatisfy(_:)

<sub>Instance Method</sub>

Publishes a single Boolean value that indicates whether all received elements pass a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allSatisfy(_ predicate: @escaping (Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>
```

## Parameters

- `predicate` — A closure that evaluates each received element. Return `true` to continue, or `false` to cancel the upstream and complete.

## Return Value

A publisher that publishes a Boolean value that indicates whether all received elements pass a given predicate.

## Discussion

Use the [allSatisfy(_:)](<allsatisfy(__).md>) operator to determine if all elements in a stream satisfy a criteria you provide. When this publisher receives an element, it runs the predicate against the element. If the predicate returns `false`, the publisher produces a `false` value and finishes. If the upstream publisher finishes normally, this publisher produces a `true` value and finishes.

In the example below, the [allSatisfy(_:)](<allsatisfy(__).md>) operator tests if each an integer array publisher’s elements fall into the `targetRange`:

```swift
let targetRange = (-1...100)
let numbers = [-1, 0, 10, 5]
numbers.publisher
    .allSatisfy { targetRange.contains($0) }
    .sink { print("\($0)") }

// Prints: "true"
```

With operators similar to [reduce(_:_:)](<reduce(____).md>), this publisher produces at most one value.

> [!note] Note
> Upon receiving any request greater than zero, this publisher requests unlimited elements from the upstream publisher.

## See Also

### Applying matching criteria to elements

- [contains(_:)](<contains(__).md>) — Publishes a Boolean value upon receiving an element equal to the argument.
- [contains(where:)](<contains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [tryContains(where:)](<trycontains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [tryAllSatisfy(_:)](<tryallsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

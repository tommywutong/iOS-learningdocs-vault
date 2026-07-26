---
title: 'output(in:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/output(in:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/output(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/output%28in%3A%29.json'
content_hash: 'sha256:7d8109228405b34a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# output(in:)

<sub>Instance Method</sub>

Publishes elements specified by their range in the sequence of published elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func output<R>(in range: R) -> Publishers.Output<Self> where R : RangeExpression, R.Bound == Int
```

## Parameters

- `range` — A range that indicates which elements to publish.

## Return Value

A publisher that publishes elements specified by a range.

## Discussion

Use [output(in:)](<output(in_).md>) to republish a range indices you specify in the published stream. After publishing all elements, the publisher finishes normally. If the publisher completes normally or with an error before producing all the elements in the range, it doesn’t publish the remaining elements.

In the example below, an array publisher emits the subset of elements at the indices in the specified range:

```swift
let numbers = [1, 1, 2, 2, 2, 3, 4, 5, 6]
numbers.publisher
    .output(in: (3...5))
    .sink { print("\($0)", terminator: " ") }

// Prints: "2 2 3"
```

## See Also

### Selecting specific elements

- [first()](<first().md>) — Publishes the first element of a stream, then finishes.
- [first(where:)](<first(where_).md>) — Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [tryFirst(where:)](<tryfirst(where_).md>) — Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [last()](<last().md>) — Publishes the last element of a stream, after the stream finishes.
- [last(where:)](<last(where_).md>) — Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [tryLast(where:)](<trylast(where_).md>) — Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [output(at:)](<output(at_).md>) — Publishes a specific element, indicated by its index in the sequence of published elements.

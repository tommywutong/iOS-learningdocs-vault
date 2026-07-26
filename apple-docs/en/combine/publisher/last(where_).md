---
title: 'last(where:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/last(where:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/last(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/last%28where%3A%29.json'
content_hash: 'sha256:0da5cc1e2cbcbb30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# last(where:)

<sub>Instance Method</sub>

Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func last(where predicate: @escaping (Self.Output) -> Bool) -> Publishers.LastWhere<Self>
```

## Parameters

- `predicate` — A closure that takes an element as its parameter and returns a Boolean value that indicates whether to publish the element.

## Return Value

A publisher that only publishes the last element satisfying the given predicate.

## Discussion

Use [last(where:)](<last(where_).md>) when you need to republish only the last element of a stream that satisfies a closure you specify.

In the example below, a range publisher emits the last element that satisfies the closure’s criteria, then finishes normally:

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .last { $0 < 6 }
    .sink { print("\($0)") }

// Prints: "5"
```

## See Also

### Selecting specific elements

- [first()](<first().md>) — Publishes the first element of a stream, then finishes.
- [first(where:)](<first(where_).md>) — Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [tryFirst(where:)](<tryfirst(where_).md>) — Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [last()](<last().md>) — Publishes the last element of a stream, after the stream finishes.
- [tryLast(where:)](<trylast(where_).md>) — Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [output(at:)](<output(at_).md>) — Publishes a specific element, indicated by its index in the sequence of published elements.
- [output(in:)](<output(in_).md>) — Publishes elements specified by their range in the sequence of published elements.

---
title: last()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/last()
source_url: 'https://developer.apple.com/documentation/combine/publisher/last()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/last%28%29.json'
content_hash: 'sha256:b9e9f403023a1553'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# last()

<sub>Instance Method</sub>

Publishes the last element of a stream, after the stream finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func last() -> Publishers.Last<Self>
```

## Return Value

A publisher that only publishes the last element of a stream.

## Discussion

Use [last()](<last().md>) when you need to emit only the last element from an upstream publisher.

In the example below, the range publisher only emits the last element from the sequence publisher, `10`, then finishes normally.

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .last()
    .sink { print("\($0)") }

// Prints: "10"
```

## See Also

### Selecting specific elements

- [first()](<first().md>) — Publishes the first element of a stream, then finishes.
- [first(where:)](<first(where_).md>) — Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [tryFirst(where:)](<tryfirst(where_).md>) — Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [last(where:)](<last(where_).md>) — Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [tryLast(where:)](<trylast(where_).md>) — Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [output(at:)](<output(at_).md>) — Publishes a specific element, indicated by its index in the sequence of published elements.
- [output(in:)](<output(in_).md>) — Publishes elements specified by their range in the sequence of published elements.

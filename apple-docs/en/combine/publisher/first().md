---
title: first()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/first()
source_url: 'https://developer.apple.com/documentation/combine/publisher/first()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/first%28%29.json'
content_hash: 'sha256:e08c5b188d6460a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# first()

<sub>Instance Method</sub>

Publishes the first element of a stream, then finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func first() -> Publishers.First<Self>
```

## Return Value

A publisher that only publishes the first element of a stream.

## Discussion

Use [first()](<first().md>) to publish just the first element from an upstream publisher, then finish normally. The [first()](<first().md>) operator requests [unlimited](../subscribers/demand/unlimited.md) from its upstream as soon as downstream requests at least one element. If the upstream completes before [first()](<first().md>) receives any elements, it completes without emitting any values.

In this example, the [first()](<first().md>) publisher republishes the first element received from the sequence publisher, `-10`, then finishes normally.

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .first()
    .sink { print("\($0)") }

// Print: "-10"
```

## See Also

### Selecting specific elements

- [first(where:)](<first(where_).md>) — Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [tryFirst(where:)](<tryfirst(where_).md>) — Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [last()](<last().md>) — Publishes the last element of a stream, after the stream finishes.
- [last(where:)](<last(where_).md>) — Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [tryLast(where:)](<trylast(where_).md>) — Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [output(at:)](<output(at_).md>) — Publishes a specific element, indicated by its index in the sequence of published elements.
- [output(in:)](<output(in_).md>) — Publishes elements specified by their range in the sequence of published elements.

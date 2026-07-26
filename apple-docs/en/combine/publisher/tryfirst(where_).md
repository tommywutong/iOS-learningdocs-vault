---
title: 'tryFirst(where:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/tryfirst(where:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/tryfirst(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/tryfirst%28where%3A%29.json'
content_hash: 'sha256:0e157c834ecf578c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryFirst(where:)

<sub>Instance Method</sub>

Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryFirst(where predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>
```

## Parameters

- `predicate` — A closure that takes an element as a parameter and returns a Boolean value that indicates whether to publish the element.

## Return Value

A publisher that only publishes the first element of a stream that satisfies the predicate.

## Discussion

Use [tryFirst(where:)](<tryfirst(where_).md>) when you need to republish only the first element of a stream that satisfies an error-throwing closure you specify. The publisher ignores all elements after the first. If this publisher doesn’t receive any elements, it finishes without publishing. If the predicate closure throws an error, the publisher fails.

In the example below, a range publisher emits the first element in the range then finishes normally:

```swift
let numberRange: ClosedRange<Int> = (-1...50)
numberRange.publisher
    .tryFirst {
        guard $0 < 99 else {throw RangeError()}
        return true
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: " ") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "-1 completion: finished"
// If instead the number range were ClosedRange<Int> = (100...200), the tryFirst operator would terminate publishing with a RangeError.
```

## See Also

### Selecting specific elements

- [first()](<first().md>) — Publishes the first element of a stream, then finishes.
- [first(where:)](<first(where_).md>) — Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [last()](<last().md>) — Publishes the last element of a stream, after the stream finishes.
- [last(where:)](<last(where_).md>) — Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [tryLast(where:)](<trylast(where_).md>) — Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [output(at:)](<output(at_).md>) — Publishes a specific element, indicated by its index in the sequence of published elements.
- [output(in:)](<output(in_).md>) — Publishes elements specified by their range in the sequence of published elements.

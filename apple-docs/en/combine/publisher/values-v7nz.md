---
title: values
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/values-v7nz
source_url: 'https://developer.apple.com/documentation/combine/publisher/values-v7nz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/values-v7nz.json'
content_hash: 'sha256:7cfdf8cf734cabbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# values

<sub>Instance Property</sub>

The elements produced by the publisher, as a throwing asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var values: AsyncThrowingPublisher<Self> { get }
```

## Discussion

This property provides an [AsyncThrowingPublisher](../asyncthrowingpublisher.md), which allows you to use the Swift `async`-`await` syntax to receive the publisher’s elements. Because [AsyncPublisher](../asyncpublisher.md) conforms to [AsyncSequence](../../swift/asyncsequence.md), you iterate over its elements with a `for`-`await`-`in` loop, rather than attaching a subscriber. If the publisher terminates with an error, the awaiting caller receives the error as a `throw`.

The following example shows how to use the `values` property to receive elements asynchronously. The example adapts a code snippet from the [tryFilter(_:)](<tryfilter(__).md>) operator’s documentation, which filters a sequence to only emit even integers, and terminate with an error on a `0`. This example replaces the [Sink](../subscribers/sink.md) subscriber with a `for`-`await`-`in` loop that iterates over the [AsyncPublisher](../asyncpublisher.md) provided by the `values` property. With this approach, the error handling previously provided in the sink subscriber’s [receiveCompletion](../subscribers/sink/receivecompletion.md) closure goes instead in a `catch` block.

```swift
let numbers: [Int] = [1, 2, 3, 4, 0, 5]
let filterPublisher = numbers.publisher
    .tryFilter{
        if $0 == 0 {
            throw ZeroError()
        } else {
            return $0 % 2 == 0
        }
    }

do {
    for try await number in filterPublisher.values {
        print ("\(number)", terminator: " ")
    }
} catch {
    print ("\(error)")
}
```

## See Also

### Accessing elements asynchronously

- [values](values-1dm9r.md) — The elements produced by the publisher, as an asynchronous sequence.

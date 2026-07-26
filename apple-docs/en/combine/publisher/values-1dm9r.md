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
doc_path: /documentation/combine/publisher/values-1dm9r
source_url: 'https://developer.apple.com/documentation/combine/publisher/values-1dm9r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/values-1dm9r.json'
content_hash: 'sha256:41ef13021ff9049e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# values

<sub>Instance Property</sub>

The elements produced by the publisher, as an asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var values: AsyncPublisher<Self> { get }
```

## Discussion

This property provides an [AsyncPublisher](../asyncpublisher.md), which allows you to use the Swift `async`-`await` syntax to receive the publisher’s elements. Because [AsyncPublisher](../asyncpublisher.md) conforms to [AsyncSequence](../../swift/asyncsequence.md), you iterate over its elements with a `for`-`await`-`in` loop, rather than attaching a subscriber.

The following example shows how to use the `values` property to receive elements asynchronously. The example adapts a code snippet from the [filter(_:)](<filter(__).md>) operator’s documentation, which filters a sequence to only emit even integers. This example replaces the [Sink](../subscribers/sink.md) subscriber with a `for`-`await`-`in` loop that iterates over the [AsyncPublisher](../asyncpublisher.md) provided by the `values` property.

```swift
let numbers: [Int] = [1, 2, 3, 4, 5]
let filtered = numbers.publisher
    .filter { $0 % 2 == 0 }

for await number in filtered.values
{
    print("\(number)", terminator: " ")
}
```

## See Also

### Accessing elements asynchronously

- [values](values-v7nz.md) — The elements produced by the publisher, as a throwing asynchronous sequence.

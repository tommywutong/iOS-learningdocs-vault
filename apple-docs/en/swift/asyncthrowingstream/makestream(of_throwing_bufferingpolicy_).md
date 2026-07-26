---
title: 'makeStream(of:throwing:bufferingPolicy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/makestream(of:throwing:bufferingpolicy:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/makestream(of:throwing:bufferingpolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/makestream%28of%3Athrowing%3Abufferingpolicy%3A%29.json'
content_hash: 'sha256:d0cf61df4d733aa9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingStream](../asyncthrowingstream.md)

# makeStream(of:throwing:bufferingPolicy:)

<sub>Type Method</sub>

Initializes a new [AsyncThrowingStream](../asyncthrowingstream.md) and an [Continuation](continuation.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 14.0, iOS 17.0, watchOS 10.0, tvOS 17.0)
static func makeStream(of elementType: Element.Type = Element.self, throwing failureType: Failure.Type = Failure.self, bufferingPolicy limit: AsyncThrowingStream<Element, Failure>.Continuation.BufferingPolicy = .unbounded) -> (stream: AsyncThrowingStream<Element, Failure>, continuation: AsyncThrowingStream<Element, Failure>.Continuation) where Failure == any Error
```

## Parameters

- `elementType` — The element type of the stream.

- `failureType` — The failure type of the stream.

- `limit` — The buffering policy that the stream should use.

## Return Value

A tuple containing the stream and its continuation. The continuation should be passed to the producer while the stream should be passed to the consumer.

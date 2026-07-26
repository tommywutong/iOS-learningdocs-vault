---
title: 'makeStream(of:bufferingPolicy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncstream/makestream(of:bufferingpolicy:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/makestream(of:bufferingpolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/makestream%28of%3Abufferingpolicy%3A%29.json'
content_hash: 'sha256:94a01809e71a9366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncStream](../asyncstream.md)

# makeStream(of:bufferingPolicy:)

<sub>Type Method</sub>

Initializes a new [AsyncStream](../asyncstream.md) and an [Continuation](continuation.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 14.0, iOS 17.0, watchOS 10.0, tvOS 17.0)
static func makeStream(of elementType: Element.Type = Element.self, bufferingPolicy limit: AsyncStream<Element>.Continuation.BufferingPolicy = .unbounded) -> (stream: AsyncStream<Element>, continuation: AsyncStream<Element>.Continuation)
```

## Parameters

- `elementType` — The element type of the stream.

- `limit` — The buffering policy that the stream should use.

## Return Value

A tuple containing the stream and its continuation. The continuation should be passed to the producer while the stream should be passed to the consumer.

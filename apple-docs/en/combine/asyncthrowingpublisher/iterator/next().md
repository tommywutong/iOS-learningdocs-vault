---
title: next()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/asyncthrowingpublisher/iterator/next()
source_url: 'https://developer.apple.com/documentation/combine/asyncthrowingpublisher/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncthrowingpublisher/iterator/next%28%29.json'
content_hash: 'sha256:938c6ffc829b8b73'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [AsyncThrowingPublisher](../../asyncthrowingpublisher.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the prefix sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws -> P.Output?
```

## Return Value

The next published element, or nil if the publisher finishes normally. If the publisher terminates with an error, the call point receives the error as a `throw`.

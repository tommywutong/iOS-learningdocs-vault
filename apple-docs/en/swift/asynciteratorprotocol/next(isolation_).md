---
title: 'next(isolation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asynciteratorprotocol/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asynciteratorprotocol/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynciteratorprotocol/next%28isolation%3A%29.json'
content_hash: 'sha256:3eb2c9f8cf91f587'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncIteratorProtocol](../asynciteratorprotocol.md)

# next(isolation:)

<sub>Instance Method</sub>

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?
```

## Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.

## Default Implementations

### AsyncIteratorProtocol Implementations

- [next(isolation:)](<next(isolation_)-6htqd.md>) — Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.

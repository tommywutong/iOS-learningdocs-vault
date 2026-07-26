---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asynciteratorprotocol/next()
source_url: 'https://developer.apple.com/documentation/swift/asynciteratorprotocol/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynciteratorprotocol/next%28%29.json'
content_hash: 'sha256:e39c03641557aabf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncIteratorProtocol](../asynciteratorprotocol.md)

# next()

<sub>Instance Method</sub>

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws -> Self.Element?
```

## Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.

## Default Implementations

### AsyncIteratorProtocol Implementations

- [next()](<next()-4a3d9.md>) — Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.

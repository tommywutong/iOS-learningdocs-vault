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
doc_path: '/documentation/swift/asynciteratorprotocol/next(isolation:)-6htqd'
source_url: 'https://developer.apple.com/documentation/swift/asynciteratorprotocol/next(isolation:)-6htqd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynciteratorprotocol/next%28isolation%3A%29-6htqd.json'
content_hash: 'sha256:0c42b3acdeba0ca6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncIteratorProtocol](../asynciteratorprotocol.md)

# next(isolation:)

<sub>Instance Method</sub>

Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?
```

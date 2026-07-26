---
title: TextOutputStreamable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/textoutputstreamable
source_url: 'https://developer.apple.com/documentation/swift/textoutputstreamable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/textoutputstreamable.json'
content_hash: 'sha256:18ad30246562d098'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# TextOutputStreamable

<sub>Protocol</sub>

A source of text-streaming operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TextOutputStreamable
```

## Overview

Instances of types that conform to the `TextOutputStreamable` protocol can write their value to instances of any type that conforms to the `TextOutputStream` protocol. The Swift standard library’s text-related types, `String`, `Character`, and `Unicode.Scalar`, all conform to `TextOutputStreamable`.

## Conforming to the TextOutputStreamable Protocol

To add `TextOutputStreamable` conformance to a custom type, implement the required `write(to:)` method. Call the given output stream’s `write(_:)` method in your implementation.

## Relationships

- **Inherited By**: [StringProtocol](stringprotocol.md)

- **Conforming Types**: [Character](character.md), [Double](double.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [String](string.md), [Substring](substring.md), [Scalar](unicode/scalar.md)

## Topics

### Instance Methods

- [write(to:)](<textoutputstreamable/write(to_).md>) — Writes a textual representation of this instance into the given output stream.

## See Also

### Streams

- [TextOutputStream](textoutputstream.md) — A type that can be the target of text-streaming operations.

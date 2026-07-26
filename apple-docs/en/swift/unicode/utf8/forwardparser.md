---
title: Unicode.UTF8.ForwardParser
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/utf8/forwardparser
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8/forwardparser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8/forwardparser.json'
content_hash: 'sha256:2dcf871f2425e48e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [UTF8](../utf8.md)

# Unicode.UTF8.ForwardParser

<sub>Structure</sub>

A type that can be used to parse `CodeUnits` into `EncodedScalar`s.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ForwardParser
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../bitwisecopyable.md), [Copyable](../../copyable.md), [Escapable](../../escapable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Initializers

- [init()](<forwardparser/init().md>) — Constructs an instance that can be used to begin parsing `CodeUnit`s at any Unicode scalar boundary.

### Type Aliases

- [Encoding](forwardparser/encoding.md) — The encoding with which this parser is associated

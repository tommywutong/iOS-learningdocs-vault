---
title: Unicode.ASCII.Parser
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/ascii/parser
source_url: 'https://developer.apple.com/documentation/swift/unicode/ascii/parser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/ascii/parser.json'
content_hash: 'sha256:7463097c126d5668'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [ASCII](../ascii.md)

# Unicode.ASCII.Parser

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Parser
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../bitwisecopyable.md), [Copyable](../../copyable.md), [Escapable](../../escapable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Initializers

- [init()](<parser/init().md>) — Constructs an instance that can be used to begin parsing `CodeUnit`s at any Unicode scalar boundary.

### Instance Methods

- [parseScalar(from:)](<parser/parsescalar(from_).md>) — Parses a single Unicode scalar value from `input`.

### Type Aliases

- [Encoding](parser/encoding.md) — The encoding with which this parser is associated

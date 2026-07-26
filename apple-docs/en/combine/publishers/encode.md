---
title: Publishers.Encode
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/encode
source_url: 'https://developer.apple.com/documentation/combine/publishers/encode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/encode.json'
content_hash: 'sha256:7e4d380b2f3962ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Encode

<sub>Structure</sub>

A publisher that encodes elements received from an upstream publisher, using a given encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Encode<Upstream, Coder> where Upstream : Publisher, Coder : TopLevelEncoder, Upstream.Output : Encodable
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a encode publisher

- [init(upstream:encoder:)](<encode/init(upstream_encoder_).md>) — Creates a publisher that decodes elements received from an upstream publisher, using a given decoder.

### Declaring supporting types

- [Output](encode/output.md) — The kind of values published by this publisher.
- [Failure](encode/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](encode/upstream.md)

## See Also

### Encoding and decoding

- [Decode](decode.md) — A publisher that decodes elements received from an upstream publisher, using a given decoder.

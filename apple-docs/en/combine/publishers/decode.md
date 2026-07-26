---
title: Publishers.Decode
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/decode
source_url: 'https://developer.apple.com/documentation/combine/publishers/decode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/decode.json'
content_hash: 'sha256:f553326250999bc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Decode

<sub>Structure</sub>

A publisher that decodes elements received from an upstream publisher, using a given decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Decode<Upstream, Output, Coder> where Upstream : Publisher, Output : Decodable, Coder : TopLevelDecoder, Upstream.Output == Coder.Input
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a decode publisher

- [init(upstream:decoder:)](<decode/init(upstream_decoder_).md>) — Creates a publisher that decodes elements received from an upstream publisher, using a given decoder.

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](decode/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](decode/upstream.md)

## See Also

### Encoding and decoding

- [Encode](encode.md) — A publisher that encodes elements received from an upstream publisher, using a given encoder.

---
title: EncodableWithConfiguration
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/encodablewithconfiguration
source_url: 'https://developer.apple.com/documentation/foundation/encodablewithconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/encodablewithconfiguration.json'
content_hash: 'sha256:9304507359d8b4ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# EncodableWithConfiguration

<sub>Protocol</sub>

A protocol for types that support encoding when supplied with an additional configuration type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol EncodableWithConfiguration
```

## Relationships

- **Conforming Types**: [AttributeContainer](attributecontainer.md), [AttributedString](attributedstring.md), [Expression](expression.md), [Predicate](predicate.md)

## Topics

### Encoding

- [encode(to:configuration:)](<encodablewithconfiguration/encode(to_configuration_).md>) — Encodes the value into the specified encoder with help from the provided configuration.

### Supporting Types

- [EncodingConfiguration](encodablewithconfiguration/encodingconfiguration.md) — The type of the encoding configuration.

## See Also

### Serializing Arbitrary Payloads

- [CodableWithConfiguration](codablewithconfiguration.md) — A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [CodableConfiguration](codableconfiguration.md) — A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [DecodableWithConfiguration](decodablewithconfiguration.md) — A protocol for types that support decoding when supplied with an additional configuration type.
- [DecodingConfigurationProviding](decodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [EncodingConfigurationProviding](encodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.

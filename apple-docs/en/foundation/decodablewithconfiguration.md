---
title: DecodableWithConfiguration
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decodablewithconfiguration
source_url: 'https://developer.apple.com/documentation/foundation/decodablewithconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decodablewithconfiguration.json'
content_hash: 'sha256:fe163a2c6d885d52'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DecodableWithConfiguration

<sub>Protocol</sub>

A protocol for types that support decoding when supplied with an additional configuration type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DecodableWithConfiguration
```

## Relationships

- **Conforming Types**: [AttributeContainer](attributecontainer.md), [AttributedString](attributedstring.md), [Expression](expression.md), [Predicate](predicate.md)

## Topics

### Decoding

- [init(from:configuration:)](<decodablewithconfiguration/init(from_configuration_).md>) — Creates a new instance by retrieving the instance’s data from the specified decoder with help from the provided configuration.

### Supporting Types

- [DecodingConfiguration](decodablewithconfiguration/decodingconfiguration.md) — The configuration type that assists in decoding.

## See Also

### Serializing Arbitrary Payloads

- [CodableWithConfiguration](codablewithconfiguration.md) — A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [CodableConfiguration](codableconfiguration.md) — A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [DecodingConfigurationProviding](decodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [EncodableWithConfiguration](encodablewithconfiguration.md) — A protocol for types that support encoding when supplied with an additional configuration type.
- [EncodingConfigurationProviding](encodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.

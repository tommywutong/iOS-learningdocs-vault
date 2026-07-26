---
title: DecodingConfigurationProviding
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decodingconfigurationproviding
source_url: 'https://developer.apple.com/documentation/foundation/decodingconfigurationproviding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decodingconfigurationproviding.json'
content_hash: 'sha256:468897f06963b3b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DecodingConfigurationProviding

<sub>Protocol</sub>

A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DecodingConfigurationProviding
```

## Relationships

- **Inherited By**: [AttributeScope](attributescope.md)

- **Conforming Types**: [AccessibilityAttributes](attributescopes/accessibilityattributes.md), [AppKitAttributes](attributescopes/appkitattributes.md), [FoundationAttributes](attributescopes/foundationattributes.md), [NumberFormatAttributes](attributescopes/foundationattributes/numberformatattributes.md), [SpeechAttributes](attributescopes/speechattributes.md), [SwiftUIAttributes](attributescopes/swiftuiattributes.md), [TranslationAttributes](attributescopes/translationattributes.md), [UIKitAttributes](attributescopes/uikitattributes.md)

## Topics

### Accessing the Configuration

- [decodingConfiguration](decodingconfigurationproviding/decodingconfiguration-swift.type.property.md) — The configuration instance that assists in decoding another type.

### Supporting Types

- [DecodingConfiguration](decodingconfigurationproviding/decodingconfiguration-swift.associatedtype.md)

## See Also

### Serializing Arbitrary Payloads

- [CodableWithConfiguration](codablewithconfiguration.md) — A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [CodableConfiguration](codableconfiguration.md) — A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [DecodableWithConfiguration](decodablewithconfiguration.md) — A protocol for types that support decoding when supplied with an additional configuration type.
- [EncodableWithConfiguration](encodablewithconfiguration.md) — A protocol for types that support encoding when supplied with an additional configuration type.
- [EncodingConfigurationProviding](encodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.

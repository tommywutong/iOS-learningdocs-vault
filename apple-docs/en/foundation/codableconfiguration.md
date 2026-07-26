---
title: CodableConfiguration
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/codableconfiguration
source_url: 'https://developer.apple.com/documentation/foundation/codableconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/codableconfiguration.json'
content_hash: 'sha256:6c77c022bf1aefed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CodableConfiguration

<sub>Structure</sub>

A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@propertyWrapper struct CodableConfiguration<T, ConfigurationProvider> where T : DecodableWithConfiguration, T : EncodableWithConfiguration, ConfigurationProvider : DecodingConfigurationProviding, ConfigurationProvider : EncodingConfigurationProviding, T.DecodingConfiguration == ConfigurationProvider.DecodingConfiguration, T.EncodingConfiguration == ConfigurationProvider.EncodingConfiguration
```

## Overview

[CodableConfiguration](codableconfiguration.md) allows you to create [Codable](../swift/codable.md) types whose members don’t all conform to [Codable](../swift/codable.md). For types that can’t support encoding and decoding by themselves but could become encodable and decodable with some statically-defined information, use the `@CodableConfiguration` wrapper. This lets you assign a configuration provider — a type that conforms to both [EncodingConfigurationProviding](encodingconfigurationproviding.md) and [DecodingConfigurationProviding](decodingconfigurationproviding.md) — to supply this data.

Limiting the [CodableConfiguration](codableconfiguration.md) to statically-defined information protects clients from loading unexpected data, similar to the protection provided by [NSSecureCoding](nssecurecoding.md).

In the following example, the `Message` type uses `@CodableConfiguration` for an [AttributedString](attributedstring.md) property called `content`. While [AttributedString](attributedstring.md) does conform to [Codable](../swift/codable.md), it can only encode its known attributes — those declared by the platform SDK — as part of this conformance. By adding a [CodableConfiguration](codableconfiguration.md) for the custom `MyAttributes` type, `Message` uses [encode(to:configuration:)](<encodablewithconfiguration/encode(to_configuration_).md>) when encoding `content`, which preserves the custom attributes.

```swift
struct Message: Codable {
    let date: Date
    let sender: Person
    @CodableConfiguration(from: MyAttributes.self) var content = AttributedString()
}
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Codable Configuration

- [init(wrappedValue:)](<codableconfiguration/init(wrappedvalue_).md>) — Creates a codable configuration wrapper for the given value.
- [init(wrappedValue:from:)](<codableconfiguration/init(wrappedvalue_from_)-46oo6.md>) — Creates a codable configuration wrapper for the given value, using the given configuration provider type.
- [init(wrappedValue:from:)](<codableconfiguration/init(wrappedvalue_from_)-8mkxk.md>) — Creates a codable configuration wrapper for the given value, using given configuration provider type identified by key path.

### Accessing the Wrapped Value

- [wrappedValue](codableconfiguration/wrappedvalue.md) — The underlying value to make codable, using data from the configuration provider.

## See Also

### Serializing Arbitrary Payloads

- [CodableWithConfiguration](codablewithconfiguration.md) — A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [DecodableWithConfiguration](decodablewithconfiguration.md) — A protocol for types that support decoding when supplied with an additional configuration type.
- [DecodingConfigurationProviding](decodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [EncodableWithConfiguration](encodablewithconfiguration.md) — A protocol for types that support encoding when supplied with an additional configuration type.
- [EncodingConfigurationProviding](encodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.

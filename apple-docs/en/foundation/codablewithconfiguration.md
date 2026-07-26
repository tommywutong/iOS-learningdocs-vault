---
title: CodableWithConfiguration
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/codablewithconfiguration
source_url: 'https://developer.apple.com/documentation/foundation/codablewithconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/codablewithconfiguration.json'
content_hash: 'sha256:1f183d5f4e07ddc1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CodableWithConfiguration

<sub>Type Alias</sub>

A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CodableWithConfiguration = DecodableWithConfiguration & EncodableWithConfiguration
```

## Discussion

[CodableWithConfiguration](codablewithconfiguration.md) is a type alias for the [EncodableWithConfiguration](encodablewithconfiguration.md) and [DecodableWithConfiguration](decodablewithconfiguration.md) protocols. Use this protocol to support codability in a type that can’t conform to [Codable](../swift/codable.md) by itself, but can do so with additional statically-defined configuration provided by a [CodableConfiguration](codableconfiguration.md) instance.

[AttributedString](attributedstring.md) uses this approach to allow an instance to contain arbitrary attributes, including frameworks outside of Foundation or the platform SDK. It does this by including one or more [AttributeScope](attributescope.md) instances, a type that conforms to [EncodingConfigurationProviding](encodingconfigurationproviding.md) and [DecodingConfigurationProviding](decodingconfigurationproviding.md). An attribute scope like [SwiftUIAttributes](attributescopes/swiftuiattributes.md) defines attribute keys, and conforms to [AttributeScope](attributescope.md) to provide configuration instances that know the [AttributedStringKey](attributedstringkey.md) types and their associated [Value](attributedstringkey/value.md) types. With this type information, an [AttributedString](attributedstring.md) can encode all of its attributes, even from frameworks other than Foundation.

## See Also

### Serializing Arbitrary Payloads

- [CodableConfiguration](codableconfiguration.md) — A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [DecodableWithConfiguration](decodablewithconfiguration.md) — A protocol for types that support decoding when supplied with an additional configuration type.
- [DecodingConfigurationProviding](decodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [EncodableWithConfiguration](encodablewithconfiguration.md) — A protocol for types that support encoding when supplied with an additional configuration type.
- [EncodingConfigurationProviding](encodingconfigurationproviding.md) — A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.

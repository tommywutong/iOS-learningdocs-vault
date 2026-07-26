---
title: 'decode(_:from:format:configuration:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistdecoder/decode(_:from:format:configuration:)-2epy4'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistdecoder/decode(_:from:format:configuration:)-2epy4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistdecoder/decode%28_%3Afrom%3Aformat%3Aconfiguration%3A%29-2epy4.json'
content_hash: 'sha256:bec403a1b9cb2f8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListDecoder](../propertylistdecoder.md)

# decode(_:from:format:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T, C>(_ type: T.Type, from data: Data, format: inout PropertyListDecoder.PropertyListFormat, configuration: C.Type) throws -> T where T : DecodableWithConfiguration, C : DecodingConfigurationProviding, T.DecodingConfiguration == C.DecodingConfiguration
```

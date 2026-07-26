---
title: 'decode(_:from:configuration:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsondecoder/decode(_:from:configuration:)-22lge'
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/decode(_:from:configuration:)-22lge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/decode%28_%3Afrom%3Aconfiguration%3A%29-22lge.json'
content_hash: 'sha256:0664a98aa6c4a2c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# decode(_:from:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T, C>(_ type: T.Type, from data: Data, configuration: C.Type) throws -> T where T : DecodableWithConfiguration, C : DecodingConfigurationProviding, T.DecodingConfiguration == C.DecodingConfiguration
```

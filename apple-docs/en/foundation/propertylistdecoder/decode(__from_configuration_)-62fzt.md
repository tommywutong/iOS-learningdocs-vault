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
doc_path: '/documentation/foundation/propertylistdecoder/decode(_:from:configuration:)-62fzt'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistdecoder/decode(_:from:configuration:)-62fzt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistdecoder/decode%28_%3Afrom%3Aconfiguration%3A%29-62fzt.json'
content_hash: 'sha256:596b22d98829cf73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListDecoder](../propertylistdecoder.md)

# decode(_:from:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_ type: T.Type, from data: Data, configuration: T.DecodingConfiguration) throws -> T where T : DecodableWithConfiguration
```

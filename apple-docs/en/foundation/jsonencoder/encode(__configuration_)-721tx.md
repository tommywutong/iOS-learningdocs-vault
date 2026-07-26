---
title: 'encode(_:configuration:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsonencoder/encode(_:configuration:)-721tx'
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/encode(_:configuration:)-721tx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/encode%28_%3Aconfiguration%3A%29-721tx.json'
content_hash: 'sha256:04905f9ab3d91231'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# encode(_:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<T, C>(_ value: T, configuration: C.Type) throws -> Data where T : EncodableWithConfiguration, C : EncodingConfigurationProviding, T.EncodingConfiguration == C.EncodingConfiguration
```

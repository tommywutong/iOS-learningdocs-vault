---
title: 'init(from:configuration:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decodablewithconfiguration/init(from:configuration:)'
source_url: 'https://developer.apple.com/documentation/foundation/decodablewithconfiguration/init(from:configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decodablewithconfiguration/init%28from%3Aconfiguration%3A%29.json'
content_hash: 'sha256:38f1e1783874891b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DecodableWithConfiguration](../decodablewithconfiguration.md)

# init(from:configuration:)

<sub>Initializer</sub>

Creates a new instance by retrieving the instance’s data from the specified decoder with help from the provided configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder, configuration: Self.DecodingConfiguration) throws
```

## Parameters

- `decoder` — The decoder to read data from.

- `configuration` — A decoding configuration instance that provides additional information necessary for decoding.

---
title: 'encode(to:configuration:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/encodablewithconfiguration/encode(to:configuration:)'
source_url: 'https://developer.apple.com/documentation/foundation/encodablewithconfiguration/encode(to:configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/encodablewithconfiguration/encode%28to%3Aconfiguration%3A%29.json'
content_hash: 'sha256:080fc26c120e80a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [EncodableWithConfiguration](../encodablewithconfiguration.md)

# encode(to:configuration:)

<sub>Instance Method</sub>

Encodes the value into the specified encoder with help from the provided configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder, configuration: Self.EncodingConfiguration) throws
```

## Parameters

- `encoder` — The encoder to write data to.

- `configuration` — An encoding configuration instance that provides additional information necessary for encoding.

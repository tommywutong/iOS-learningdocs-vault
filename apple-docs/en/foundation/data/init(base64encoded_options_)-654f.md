---
title: 'init(base64Encoded:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(base64encoded:options:)-654f'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(base64encoded:options:)-654f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28base64encoded%3Aoptions%3A%29-654f.json'
content_hash: 'sha256:66e30ecefbce0e16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(base64Encoded:options:)

<sub>Initializer</sub>

Initialize a `Data` from a Base-64 encoded String using the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(base64Encoded base64String: String, options: Data.Base64DecodingOptions = [])
```

## Parameters

- `base64String` — The string to parse.

- `options` — Encoding options. Default value is `[]`.

## Discussion

Returns nil when the input is not recognized as valid Base-64.

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
doc_path: '/documentation/foundation/data/init(base64encoded:options:)-1g88z'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(base64encoded:options:)-1g88z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28base64encoded%3Aoptions%3A%29-1g88z.json'
content_hash: 'sha256:f54b9e3483bc0ae8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(base64Encoded:options:)

<sub>Initializer</sub>

Initialize a `Data` from a Base-64, UTF-8 encoded `Data`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(base64Encoded base64Data: Data, options: Data.Base64DecodingOptions = [])
```

## Parameters

- `base64Data` — Base-64, UTF-8 encoded input data.

- `options` — Decoding options. Default value is `[]`.

## Discussion

Returns nil when the input is not recognized as valid Base-64.

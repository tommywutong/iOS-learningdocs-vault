---
title: 'base64EncodedString(options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/base64encodedstring(options:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/base64encodedstring(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/base64encodedstring%28options%3A%29.json'
content_hash: 'sha256:cf3aa765d4237f27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# base64EncodedString(options:)

<sub>Instance Method</sub>

Returns a Base-64 encoded string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func base64EncodedString(options: Data.Base64EncodingOptions = []) -> String
```

## Parameters

- `options` — The options to use for the encoding. Default value is `[]`.

## Return Value

The Base-64 encoded string.

## See Also

### Base-64 Encoding

- [base64EncodedData(options:)](<base64encodeddata(options_).md>) — Returns Base-64 encoded data.
- [Base64DecodingOptions](base64decodingoptions.md) — Options to use when decoding data.
- [Base64EncodingOptions](base64encodingoptions.md) — Options to use when encoding data.

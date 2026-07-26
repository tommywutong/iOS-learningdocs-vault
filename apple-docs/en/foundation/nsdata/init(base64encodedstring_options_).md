---
title: 'init(base64EncodedString:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(base64encodedstring:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(base64encodedstring:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28base64encodedstring%3Aoptions%3A%29.json'
content_hash: 'sha256:27c22f9d3f791e3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(base64EncodedString:options:)

<sub>Initializer</sub>

Initializes a data object with the given Base64 encoded string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(base64EncodedString base64String: String, options: NSData.Base64DecodingOptions = [])
```

## Parameters

- `base64String` — A Base-64 encoded string.

- `options` — A mask that specifies options for Base-64 decoding the data. Possible values are given in [Base64DecodingOptions](base64decodingoptions.md).

## Return Value

A data object built by Base64 decoding the provided string. Returns `nil` if the data object could not be decoded.

## Discussion

The default implementation of this method will reject non-alphabet characters, including line break characters. To support different encodings and ignore non-alphabet characters, specify an `options` value of [NSDataBase64DecodingIgnoreUnknownCharacters](base64decodingoptions/ignoreunknowncharacters.md).

## See Also

### Encoding and Decoding Base64 Representations

- [init(base64EncodedData:options:)](<init(base64encodeddata_options_).md>) — Initializes a data object with the given Base64 encoded data.
- [- initWithBase64Encoding:](<init(base64encoding_).md>) — Initializes a data object initialized with the given Base64 encoded string. _(deprecated)_
- [- base64EncodedDataWithOptions:](<base64encodeddata(options_).md>) — Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [- base64EncodedStringWithOptions:](<base64encodedstring(options_).md>) — Creates a Base64 encoded string from the string using the given options.
- [- base64Encoding](<base64encoding().md>) — Initializes a Base64 encoded string from the string. _(deprecated)_
- [Base64EncodingOptions](base64encodingoptions.md) — Options for methods used to Base64 encode data.
- [Base64DecodingOptions](base64decodingoptions.md) — Options to modify the decoding algorithm used to decode Base64 encoded data.

---
title: 'base64EncodedData(options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/base64encodeddata(options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/base64encodeddata(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/base64encodeddata%28options%3A%29.json'
content_hash: 'sha256:8134b9f22bf8e88c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# base64EncodedData(options:)

<sub>Instance Method</sub>

Creates a Base64, UTF-8 encoded data object from the string using the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func base64EncodedData(options: NSData.Base64EncodingOptions = []) -> Data
```

## Parameters

- `options` — A mask that specifies options for Base64 encoding the data. Possible values are given in [Base64EncodingOptions](base64encodingoptions.md).

## Return Value

A Base64, UTF-8 encoded data object.

## Discussion

By default, no line endings are inserted.

If you specify one of the line length options ([NSDataBase64Encoding64CharacterLineLength](base64encodingoptions/linelength64characters.md) or [NSDataBase64Encoding76CharacterLineLength](base64encodingoptions/linelength76characters.md)) but don’t specify the kind of line ending to insert, the default line ending is Carriage Return + Line Feed.

## See Also

### Encoding and Decoding Base64 Representations

- [init(base64EncodedData:options:)](<init(base64encodeddata_options_).md>) — Initializes a data object with the given Base64 encoded data.
- [- initWithBase64Encoding:](<init(base64encoding_).md>) — Initializes a data object initialized with the given Base64 encoded string. _(deprecated)_
- [init(base64EncodedString:options:)](<init(base64encodedstring_options_).md>) — Initializes a data object with the given Base64 encoded string.
- [- base64EncodedStringWithOptions:](<base64encodedstring(options_).md>) — Creates a Base64 encoded string from the string using the given options.
- [- base64Encoding](<base64encoding().md>) — Initializes a Base64 encoded string from the string. _(deprecated)_
- [Base64EncodingOptions](base64encodingoptions.md) — Options for methods used to Base64 encode data.
- [Base64DecodingOptions](base64decodingoptions.md) — Options to modify the decoding algorithm used to decode Base64 encoded data.

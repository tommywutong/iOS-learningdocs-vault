---
title: base64Encoding()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdata/base64encoding()
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/base64encoding()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/base64encoding%28%29.json'
content_hash: 'sha256:d8211c94c862c0a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# base64Encoding()

<sub>Instance Method</sub>

Initializes a Base64 encoded string from the string.

> [!warning] Deprecated
> You should transition to either [- base64EncodedStringWithOptions:](<base64encodedstring(options_).md>) or [- base64EncodedDataWithOptions:](<base64encodeddata(options_).md>)

<sub>tvOS, visionOS, watchOS</sub>

```swift
func base64Encoding() -> String
```

## Return Value

A Base-64 encoded string.

## Discussion

This method is equivalent to calling [- base64EncodedStringWithOptions:](<base64encodedstring(options_).md>) with no options specified.

### Special Considerations

Although this method was only introduced publicly for iOS 7, it has existed since iOS 4; you can use it if your application needs to target an operating system prior to iOS 7.

## See Also

### Encoding and Decoding Base64 Representations

- [init(base64EncodedData:options:)](<init(base64encodeddata_options_).md>) — Initializes a data object with the given Base64 encoded data.
- [- initWithBase64Encoding:](<init(base64encoding_).md>) — Initializes a data object initialized with the given Base64 encoded string. _(deprecated)_
- [init(base64EncodedString:options:)](<init(base64encodedstring_options_).md>) — Initializes a data object with the given Base64 encoded string.
- [- base64EncodedDataWithOptions:](<base64encodeddata(options_).md>) — Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [- base64EncodedStringWithOptions:](<base64encodedstring(options_).md>) — Creates a Base64 encoded string from the string using the given options.
- [Base64EncodingOptions](base64encodingoptions.md) — Options for methods used to Base64 encode data.
- [Base64DecodingOptions](base64decodingoptions.md) — Options to modify the decoding algorithm used to decode Base64 encoded data.

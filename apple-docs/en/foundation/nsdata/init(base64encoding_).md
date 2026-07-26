---
title: 'init(base64Encoding:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdata/init(base64encoding:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(base64encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28base64encoding%3A%29.json'
content_hash: 'sha256:95ccc091289d01cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(base64Encoding:)

<sub>Initializer</sub>

Initializes a data object initialized with the given Base64 encoded string.

> [!warning] Deprecated
> You should transition to either [init(base64EncodedString:options:)](<init(base64encodedstring_options_).md>) or [init(base64EncodedData:options:)](<init(base64encodeddata_options_).md>).

<sub>tvOS, visionOS, watchOS</sub>

```swift
init?(base64Encoding base64String: String)
```

## Parameters

- `base64String` — A Base-64 encoded string.

## Return Value

A data object built by Base-64 decoding the provided string. Returns `nil` if the data object could not be decoded.

## Discussion

Although this method was only introduced publicly for iOS 7, it has existed since iOS 4; you can use it if your application needs to target an operating system prior to iOS 7. This method behaves like [init(base64EncodedString:options:)](<init(base64encodedstring_options_).md>), but ignores all unknown characters.

## See Also

### Encoding and Decoding Base64 Representations

- [init(base64EncodedData:options:)](<init(base64encodeddata_options_).md>) — Initializes a data object with the given Base64 encoded data.
- [init(base64EncodedString:options:)](<init(base64encodedstring_options_).md>) — Initializes a data object with the given Base64 encoded string.
- [- base64EncodedDataWithOptions:](<base64encodeddata(options_).md>) — Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [- base64EncodedStringWithOptions:](<base64encodedstring(options_).md>) — Creates a Base64 encoded string from the string using the given options.
- [- base64Encoding](<base64encoding().md>) — Initializes a Base64 encoded string from the string. _(deprecated)_
- [Base64EncodingOptions](base64encodingoptions.md) — Options for methods used to Base64 encode data.
- [Base64DecodingOptions](base64decodingoptions.md) — Options to modify the decoding algorithm used to decode Base64 encoded data.

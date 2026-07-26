---
title: NSData.Base64DecodingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/base64decodingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/base64decodingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/base64decodingoptions.json'
content_hash: 'sha256:cfe0bc2c385752bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# NSData.Base64DecodingOptions

<sub>Structure</sub>

Options to modify the decoding algorithm used to decode Base64 encoded data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Base64DecodingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<base64decodingoptions/init(rawvalue_).md>)

### Constants

- [NSDataBase64DecodingIgnoreUnknownCharacters](base64decodingoptions/ignoreunknowncharacters.md) — Modify the decoding algorithm so that it ignores unknown non-Base-64 bytes, including line ending characters.

## See Also

### Encoding and Decoding Base64 Representations

- [init(base64EncodedData:options:)](<init(base64encodeddata_options_).md>) — Initializes a data object with the given Base64 encoded data.
- [- initWithBase64Encoding:](<init(base64encoding_).md>) — Initializes a data object initialized with the given Base64 encoded string. _(deprecated)_
- [init(base64EncodedString:options:)](<init(base64encodedstring_options_).md>) — Initializes a data object with the given Base64 encoded string.
- [- base64EncodedDataWithOptions:](<base64encodeddata(options_).md>) — Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [- base64EncodedStringWithOptions:](<base64encodedstring(options_).md>) — Creates a Base64 encoded string from the string using the given options.
- [- base64Encoding](<base64encoding().md>) — Initializes a Base64 encoded string from the string. _(deprecated)_
- [Base64EncodingOptions](base64encodingoptions.md) — Options for methods used to Base64 encode data.

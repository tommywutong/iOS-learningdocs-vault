---
title: 'init(base64Encoded:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(base64encoded:options:)-3ksry'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(base64encoded:options:)-3ksry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28base64encoded%3Aoptions%3A%29-3ksry.json'
content_hash: 'sha256:1a727f1f418aa705'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(base64Encoded:options:)

<sub>Initializer</sub>

Initializes a data object with the given Base64 encoded string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(base64Encoded base64String: String, options: NSData.Base64DecodingOptions = [])
```

## Parameters

- `base64String` — A Base-64 encoded string.

- `options` — A mask that specifies options for Base-64 decoding the data. Possible values are given in [Base64DecodingOptions](base64decodingoptions.md).

## Return Value

A data object built by Base64 decoding the provided string. Returns `nil` if the data object could not be decoded.

## Discussion

The default implementation of this method will reject non-alphabet characters, including line break characters. To support different encodings and ignore non-alphabet characters, specify an `options` value of [NSDataBase64DecodingIgnoreUnknownCharacters](base64decodingoptions/ignoreunknowncharacters.md).

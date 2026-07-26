---
title: 'init(RTF:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(rtf:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(rtf:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28rtf%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:da23e937c4687a59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(RTF:documentAttributes:)

<sub>Initializer</sub>

Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.

<sub>macOS</sub>

```swift
init?(RTF data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

<sub>macOS</sub>

```swift
init?(rtf data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `data` — The data containing RTF content.

- `dict` — An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

## Discussion

Also returns by reference in `dict` a dictionary containing document-level attributes described in [DocumentAttributeKey](documentattributekey.md). `dict` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if `data` can’t be decoded.

## See Also

### Creating from RTF

- [- initWithRTFD:documentAttributes:](<init(rtfd_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.
- [- initWithRTFDFileWrapper:documentAttributes:](<init(rtfdfilewrapper_documentattributes_).md>) — Creates an attributed string from the specified file wrapper that contains an RTFD document.

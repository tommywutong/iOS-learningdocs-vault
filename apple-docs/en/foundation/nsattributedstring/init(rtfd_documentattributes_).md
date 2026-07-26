---
title: 'init(RTFD:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(rtfd:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(rtfd:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28rtfd%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:4dc43225cbfb7196'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(RTFD:documentAttributes:)

<sub>Initializer</sub>

Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.

<sub>macOS</sub>

```swift
init?(RTFD data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

<sub>macOS</sub>

```swift
init?(rtfd data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `data` — The data containing the RTFD content.

- `dict` — An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

## See Also

### Creating from RTF

- [- initWithRTF:documentAttributes:](<init(rtf_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [- initWithRTFDFileWrapper:documentAttributes:](<init(rtfdfilewrapper_documentattributes_).md>) — Creates an attributed string from the specified file wrapper that contains an RTFD document.

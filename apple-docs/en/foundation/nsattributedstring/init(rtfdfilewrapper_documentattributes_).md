---
title: 'init(RTFDFileWrapper:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(rtfdfilewrapper:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(rtfdfilewrapper:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28rtfdfilewrapper%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:e5ea6e3285e88359'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(RTFDFileWrapper:documentAttributes:)

<sub>Initializer</sub>

Creates an attributed string from the specified file wrapper that contains an RTFD document.

<sub>macOS</sub>

```swift
init?(RTFDFileWrapper wrapper: FileWrapper, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

<sub>macOS</sub>

```swift
init?(rtfdFileWrapper wrapper: FileWrapper, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `wrapper` — The [FileWrapper](../filewrapper.md) containing the RTFD document.

- `dict` — An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

## Discussion

Also returns by reference in `dict` a dictionary containing document-level attributes described in [DocumentAttributeKey](documentattributekey.md). `dict` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if `wrapper` can’t be interpreted as an RTFD document.

## See Also

### Creating from RTF

- [- initWithRTF:documentAttributes:](<init(rtf_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [- initWithRTFD:documentAttributes:](<init(rtfd_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.

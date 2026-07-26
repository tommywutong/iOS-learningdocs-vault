---
title: 'init(docFormat:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(docformat:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(docformat:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28docformat%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:25dc550bf7520d3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(docFormat:documentAttributes:)

<sub>Initializer</sub>

Creates an attributed string from Microsoft Word format data in the specified data object.

<sub>macOS</sub>

```swift
init?(docFormat data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `data` — The data from which to create the string.

- `dict` — An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

## See Also

### Creating from a data file

- [- initWithData:options:documentAttributes:error:](<init(data_options_documentattributes_).md>) — Creates an attributed string from the contents of the specified data object.
- [- initWithURL:options:documentAttributes:error:](<init(url_options_documentattributes_).md>) — Creates an attributed string from the contents of the specified URL.

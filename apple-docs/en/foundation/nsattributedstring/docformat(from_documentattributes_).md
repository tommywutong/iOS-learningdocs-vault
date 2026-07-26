---
title: 'docFormat(from:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/docformat(from:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/docformat(from:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/docformat%28from%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:db24b726f58bfd18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# docFormat(from:documentAttributes:)

<sub>Instance Method</sub>

Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.

<sub>macOS</sub>

```swift
func docFormat(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> Data?
```

## Parameters

- `range` — The range.

- `dict` — A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain [documentType](documentattributekey/documenttype.md).

## Return Value

Returns a data object containing the attributed string as a Microsoft Word doc file.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Exporting the string as data

- [- dataFromRange:documentAttributes:error:](<data(from_documentattributes_).md>) — Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- fileWrapperFromRange:documentAttributes:error:](<filewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- RTFFromRange:documentAttributes:](<rtf(from_documentattributes_).md>) — Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [- RTFDFromRange:documentAttributes:](<rtfd(from_documentattributes_).md>) — Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [- RTFDFileWrapperFromRange:documentAttributes:](<rtfdfilewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.

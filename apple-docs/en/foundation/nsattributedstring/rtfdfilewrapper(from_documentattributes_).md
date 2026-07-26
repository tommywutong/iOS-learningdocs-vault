---
title: 'rtfdFileWrapper(from:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/rtfdfilewrapper(from:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/rtfdfilewrapper(from:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/rtfdfilewrapper%28from%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:1cc7af0c4f7c73ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# rtfdFileWrapper(from:documentAttributes:)

<sub>Instance Method</sub>

Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.

<sub>macOS</sub>

```swift
func rtfdFileWrapper(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> FileWrapper?
```

## Parameters

- `range` — The range.

- `dict` — A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain `NSDocumentTypeDocumentAttribute`.

## Return Value

A file wrapper containing the RTFD data.

## Discussion

The file wrapper also includes the document-level attributes in `docAttributes`, as explained in [RTF Files and Attributed Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/RTFAndAttrStrings.html#//apple_ref/doc/uid/20000164).

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

You can save the file wrapper using the [- writeToFile:atomically:updateFilenames:](<../filewrapper/write(tofile_atomically_updatefilenames_).md>) method of [FileWrapper](../filewrapper.md).

## See Also

### Exporting the string as data

- [- dataFromRange:documentAttributes:error:](<data(from_documentattributes_).md>) — Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- fileWrapperFromRange:documentAttributes:error:](<filewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- docFormatFromRange:documentAttributes:](<docformat(from_documentattributes_).md>) — Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [- RTFFromRange:documentAttributes:](<rtf(from_documentattributes_).md>) — Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [- RTFDFromRange:documentAttributes:](<rtfd(from_documentattributes_).md>) — Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.

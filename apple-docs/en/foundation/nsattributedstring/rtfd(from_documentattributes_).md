---
title: 'rtfd(from:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/rtfd(from:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/rtfd(from:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/rtfd%28from%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:5c671d3be4d4c20d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# rtfd(from:documentAttributes:)

<sub>Instance Method</sub>

Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.

<sub>macOS</sub>

```swift
func rtfd(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> Data?
```

## Parameters

- `range` — The range.

- `dict` — A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain [documentType](documentattributekey/documenttype.md).

## Return Value

A data object containing the RTFD stream containing the characters and attributes.

## Discussion

Writes the document-level attributes in `docAttributes`, as explained in [RTF Files and Attributed Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/RTFAndAttrStrings.html#//apple_ref/doc/uid/20000164).

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

When writing data to the pasteboard, you can use the `NSData` object as the first argument to the [NSPasteboard](../../appkit/nspasteboard.md) method [setData(_:forType:)](<../../appkit/nspasteboard/setdata(__fortype_).md>), with a second argument of `NSRTFPboardType`.

## See Also

### Exporting the string as data

- [- dataFromRange:documentAttributes:error:](<data(from_documentattributes_).md>) — Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- fileWrapperFromRange:documentAttributes:error:](<filewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- docFormatFromRange:documentAttributes:](<docformat(from_documentattributes_).md>) — Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [- RTFFromRange:documentAttributes:](<rtf(from_documentattributes_).md>) — Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [- RTFDFileWrapperFromRange:documentAttributes:](<rtfdfilewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.

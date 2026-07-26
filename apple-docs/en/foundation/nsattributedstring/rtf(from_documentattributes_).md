---
title: 'rtf(from:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/rtf(from:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/rtf(from:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/rtf%28from%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:5db1aba08e5c5972'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# rtf(from:documentAttributes:)

<sub>Instance Method</sub>

Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.

<sub>macOS</sub>

```swift
func rtf(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> Data?
```

## Parameters

- `range` — The range.

- `dict` — A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain [documentType](documentattributekey/documenttype.md).

## Return Value

A data object containing an RTF stream for the attributed string.

## Discussion

Writes the document-level attributes in `docAttributes`, as explained in [RTF Files and Attributed Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/RTFAndAttrStrings.html#//apple_ref/doc/uid/20000164).

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

When writing data to the pasteboard, you can use the `NSData` object as the first argument to the [NSPasteboard](../../appkit/nspasteboard.md) method [setData(_:forType:)](<../../appkit/nspasteboard/setdata(__fortype_).md>), with a second argument of `NSRTFPboardType`. Although this method strips attachments, it leaves the attachment characters in the text itself. The `NSText` method  [rtf(from:)](<../../appkit/nstext/rtf(from_).md>), on the other hand, does strip attachment characters when extracting RTF.

## See Also

### Exporting the string as data

- [- dataFromRange:documentAttributes:error:](<data(from_documentattributes_).md>) — Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- fileWrapperFromRange:documentAttributes:error:](<filewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- docFormatFromRange:documentAttributes:](<docformat(from_documentattributes_).md>) — Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [- RTFDFromRange:documentAttributes:](<rtfd(from_documentattributes_).md>) — Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [- RTFDFileWrapperFromRange:documentAttributes:](<rtfdfilewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.

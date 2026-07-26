---
title: 'fileWrapper(from:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/filewrapper(from:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/filewrapper(from:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/filewrapper%28from%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:b7e9d2dc9455e451'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# fileWrapper(from:documentAttributes:)

<sub>Instance Method</sub>

Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fileWrapper(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) throws -> FileWrapper
```

## Parameters

- `range` — The range.

- `dict` — A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain [documentType](documentattributekey/documenttype.md).

## Return Value

Returns a file wrapper for the appropriate document type, or `nil` if failure. When `nil`, `error` encapsulates the error information.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Exporting the string as data

- [- dataFromRange:documentAttributes:error:](<data(from_documentattributes_).md>) — Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [- docFormatFromRange:documentAttributes:](<docformat(from_documentattributes_).md>) — Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [- RTFFromRange:documentAttributes:](<rtf(from_documentattributes_).md>) — Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [- RTFDFromRange:documentAttributes:](<rtfd(from_documentattributes_).md>) — Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [- RTFDFileWrapperFromRange:documentAttributes:](<rtfdfilewrapper(from_documentattributes_).md>) — Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.

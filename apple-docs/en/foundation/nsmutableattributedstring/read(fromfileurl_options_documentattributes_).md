---
title: 'read(fromFileURL:options:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmutableattributedstring/read(fromfileurl:options:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(fromfileurl:options:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/read%28fromfileurl%3Aoptions%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:0f70a07500f190d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# read(fromFileURL:options:documentAttributes:)

<sub>Instance Method</sub>

Sets the contents of the receiver from the file at the given URL.

> [!warning] Deprecated
> Use [- readFromURL:options:documentAttributes:error:](<read(from_options_documentattributes_)-54wth.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
func read(fromFileURL url: URL, options opts: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

## Parameters

- `url` — The location of the file providing text data.

- `opts` — The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in [NSAttributedString](../nsattributedstring.md).

- `dict` — On return, contains the document attributes. For a list of possible values, see “Document Attributes” in [NSAttributedString](../nsattributedstring.md).

## Discussion

For RTF formatted files, the contents of the file are appended to the previous string instead of replacing the previous string.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated

- [- readFromData:options:documentAttributes:](<read(from_options_documentattributes_)-967j7.md>) — Sets the contents of the receiver from the specified data object`.` _(deprecated)_
- [- readFromURL:options:documentAttributes:](<read(from_options_documentattributes_)-85y1d.md>) — Sets the contents of receiver from the file at the specified URL. _(deprecated)_

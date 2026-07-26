---
title: 'read(from:options:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-54wth'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-54wth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/read%28from%3Aoptions%3Adocumentattributes%3A%29-54wth.json'
content_hash: 'sha256:135fe08e3605838f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# read(from:options:documentAttributes:)

<sub>Instance Method</sub>

Sets the contents of attributed string using the contents of the specified file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func read(from url: URL, options opts: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

<sub>macOS</sub>

```swift
func read(from url: URL, options opts: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?, error: ()) throws
```

## Parameters

- `url` — The URL of the file to read.

- `opts` — The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in [NSAttributedString](../nsattributedstring.md).

- `dict` — On return, contains the document attributes. For a list of possible values, see “Document Attributes” in [NSAttributedString](../nsattributedstring.md).

- `error` — Upon return, if an error occurs, contains an [NSError](../nserror.md) object that describes the problem. If you are not interested in possible errors, pass in `NULL`.

## Discussion

Filter services can be used to convert the contents of the URL into a format recognized by Cocoa.

For RTF formatted files, the contents of the file are appended to the previous string instead of replacing the previous string. Therefore, when using this method with existing content it’s best to clear the content away explicitly.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Reading Content

- [- readFromData:options:documentAttributes:error:](<read(from_options_documentattributes_)-5mbcx.md>) — Sets the contents of the attributed string using the specified data object`.`

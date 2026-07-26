---
title: 'read(from:options:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-5mbcx'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-5mbcx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/read%28from%3Aoptions%3Adocumentattributes%3A%29-5mbcx.json'
content_hash: 'sha256:a2dceb8f5b8d6a6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# read(from:options:documentAttributes:)

<sub>Instance Method</sub>

Sets the contents of the attributed string using the specified data object`.`

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func read(from data: Data, options opts: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

<sub>macOS</sub>

```swift
func read(from data: Data, options opts: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?, error: ()) throws
```

## Parameters

- `data` — The data object providing text data.

- `opts` — Keys specifying the types of documents and other document import options. For a list of possible values, see “Option keys for importing documents” in [NSAttributedString](../nsattributedstring.md)

- `dict` — On return, the dictionary (if provided) contains keys representing various document-wide attributes. For a list of possible values, see “Document Attributes” in [NSAttributedString](../nsattributedstring.md).

- `error` — Upon return, if an error occurs, contains an `NSError` object that describes the problem. If you are not interested in possible errors, pass in `NULL`.

## Discussion

`opts` can contain one of the values described in the Constants section of NSAttributedString Application Kit Additions Reference (“Option keys for importing documents”).

On return, the `documentAttributes` dictionary (if provided) contains the various keys described in the Constants section of NSAttributedString Application Kit Additions Reference. If unsuccessful, returns NO , after setting `error` to point to an `NSError` object that encapsulates the reason why the attributed string object could not be created.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Reading Content

- [- readFromURL:options:documentAttributes:error:](<read(from_options_documentattributes_)-54wth.md>) — Sets the contents of attributed string using the contents of the specified file.

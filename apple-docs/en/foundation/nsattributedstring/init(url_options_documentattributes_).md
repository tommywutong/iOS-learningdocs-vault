---
title: 'init(URL:options:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(url:options:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(url:options:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28url%3Aoptions%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:19aa204afa8b2d1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(URL:options:documentAttributes:)

<sub>Initializer</sub>

Creates an attributed string from the contents of the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(URL url: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(url: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

## Parameters

- `url` — An `NSURL` object specifying the document to load.

- `options` — Attributes for interpreting the document contents. Specify the [documentType](documentattributekey/documenttype.md) or [fileType](documentreadingoptionkey/filetype.md) option to interpret the data as a specific type. When sharing files between different platforms, specify the [sourceTextScaling](documentreadingoptionkey/sourcetextscaling.md) or [targetTextScaling](documentreadingoptionkey/targettextscaling.md) options for any required text scaling behaviors. Specify the [characterEncoding](documentattributekey/characterencoding.md) attribute for plain-text files. Specify the [defaultAttributes](documentattributekey/defaultattributes.md) key to apply document attributes to the returned string. If you specify an empty dictionary, the method identifies the data format from the data itself.

- `dict` — An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

## Discussion

Filter services can be used to convert the file into a format recognized by Cocoa. The `options` dictionary specifies how the document should be loaded and can contain the values described in [NSAttributedStringDocumentReadingOptionKey](../../uikit/nsattributedstringdocumentreadingoptionkey.md). If you specify the [documentType](documentreadingoptionkey/documenttype.md) or [fileType](documentreadingoptionkey/filetype.md) attribute, this method treats the data as if it is in the specified format. If you don’t specify one of these options, the method examines the document and loads it using whatever format it seems to contain.

If an error occurs, the method returns `nil` and sets the `error` parameter to an [NSError](../nserror.md) object with information about why it couldn’t create the attributed string object.

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Creating from a data file

- [- initWithData:options:documentAttributes:error:](<init(data_options_documentattributes_).md>) — Creates an attributed string from the contents of the specified data object.
- [- initWithDocFormat:documentAttributes:](<init(docformat_documentattributes_).md>) — Creates an attributed string from Microsoft Word format data in the specified data object.

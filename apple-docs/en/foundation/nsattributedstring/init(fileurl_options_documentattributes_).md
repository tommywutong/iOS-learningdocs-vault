---
title: 'init(fileURL:options:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsattributedstring/init(fileurl:options:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(fileurl:options:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28fileurl%3Aoptions%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:49df48817dea08dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(fileURL:options:documentAttributes:)

<sub>Initializer</sub>

Initializes a new attributed string object from the data at the specified URL.

> [!warning] Deprecated
> Use [- initWithURL:options:documentAttributes:error:](<init(url_options_documentattributes_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
init(fileURL url: URL, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

## Parameters

- `url` — An `NSURL` object specifying the document to load.

- `options` — Document attributes for interpreting the document contents. [documentType](documentattributekey/documenttype.md), [characterEncoding](documentattributekey/characterencoding.md), and [defaultAttributes](documentattributekey/defaultattributes.md) are supported option keys. If not specified, the method examines the data to attempt to determine the appropriate attributes.

- `dict` — If non-`NULL`, returns a dictionary with various document-wide attributes accessible via document attribute keys.

## Return Value

Returns an initialized attributed string object, or `nil` if the data can’t be decoded.

## Discussion

The HTML importer should not be called from a background thread (that is, the `options` dictionary includes [documentType](documentattributekey/documenttype.md) with a value of [html](documenttype/html.md)). It will try to synchronize with the main thread, fail, and time out. Calling it from the main thread works (but can still time out if the HTML contains references to external resources, which should be avoided at all costs). The HTML import mechanism is meant for implementing something like markdown (that is, text styles, colors, and so on), not for general HTML import.

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated Initializers

- [- initWithPath:documentAttributes:](<init(path_documentattributes_).md>) — Initializes a new attribute string object from RTF or RTFD data in the file at the specified path. _(deprecated)_
- [- initWithURL:documentAttributes:](<init(url_documentattributes_).md>) — Initializes a new attributed string object from the data at the specified URL. _(deprecated)_

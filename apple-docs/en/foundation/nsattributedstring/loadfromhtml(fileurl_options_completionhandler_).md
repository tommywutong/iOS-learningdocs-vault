---
title: 'loadFromHTML(fileURL:options:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/loadfromhtml(fileurl:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/loadfromhtml(fileurl:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/loadfromhtml%28fileurl%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:6d81975b529c4cc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# loadFromHTML(fileURL:options:completionHandler:)

<sub>Type Method</sub>

Creates an attributed string by converting the content of a local HTML file at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func loadFromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], completionHandler: @escaping @Sendable (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func fromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:]) async throws -> (NSAttributedString, [NSAttributedString.DocumentAttributeKey : Any])
```

## Parameters

- `fileURL` — A URL that specifies the file to load.

- `options` — Specifies additional options for loading the document. For a list of possible keys, see [NSAttributedStringDocumentReadingOptionKey](../../uikit/nsattributedstringdocumentreadingoptionkey.md).

- `completionHandler` — A completion handler to execute with the results.

## See Also

### Creating from HTML

- [- initWithHTML:documentAttributes:](<init(html_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object.
- [- initWithHTML:baseURL:documentAttributes:](<init(html_baseurl_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object and base URL.
- [- initWithHTML:options:documentAttributes:](<init(html_options_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object.
- [+ loadFromHTMLWithRequest:options:completionHandler:](<loadfromhtml(request_options_completionhandler_).md>) — Creates an attributed string by converting the contents of the specified HTML URL request.
- [+ loadFromHTMLWithString:options:completionHandler:](<loadfromhtml(string_options_completionhandler_).md>) — Creates an attributed string from the specified HTML string.
- [+ loadFromHTMLWithData:options:completionHandler:](<loadfromhtml(data_options_completionhandler_).md>) — Creates an attributed string from the specified HTML data.
- [CompletionHandler](completionhandler.md) — A completion handler for getting an asynchronous attributed string.

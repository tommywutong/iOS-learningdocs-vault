---
title: NSAttributedString.CompletionHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/completionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/completionhandler.json'
content_hash: 'sha256:debd9322936772ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.CompletionHandler

<sub>Type Alias</sub>

A completion handler for getting an asynchronous attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
typealias CompletionHandler = (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void
```

## Parameters

- `attributedString` — The attributed string, or nil if the method couldn’t create the string.

- `attributes` — A dictionary containing document-level attributes. This parameter is `nil` if the document doesn’t have any attributes.

- `error` — An error object if an error occurred, or `nil` if the method returned the string successfully.

## See Also

### Creating from HTML

- [- initWithHTML:documentAttributes:](<init(html_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object.
- [- initWithHTML:baseURL:documentAttributes:](<init(html_baseurl_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object and base URL.
- [- initWithHTML:options:documentAttributes:](<init(html_options_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object.
- [+ loadFromHTMLWithRequest:options:completionHandler:](<loadfromhtml(request_options_completionhandler_).md>) — Creates an attributed string by converting the contents of the specified HTML URL request.
- [+ loadFromHTMLWithFileURL:options:completionHandler:](<loadfromhtml(fileurl_options_completionhandler_).md>) — Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [+ loadFromHTMLWithString:options:completionHandler:](<loadfromhtml(string_options_completionhandler_).md>) — Creates an attributed string from the specified HTML string.
- [+ loadFromHTMLWithData:options:completionHandler:](<loadfromhtml(data_options_completionhandler_).md>) — Creates an attributed string from the specified HTML data.

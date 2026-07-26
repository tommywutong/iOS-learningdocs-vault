---
title: 'init(HTML:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(html:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(html:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28html%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:2e3f5b3dfd59e779'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(HTML:documentAttributes:)

<sub>Initializer</sub>

Creates an attributed string from the HTML in the specified data object.

<sub>macOS</sub>

```swift
init?(HTML data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

<sub>macOS</sub>

```swift
init?(html data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `data` — A data object with text in HTML format. The method uses this data to create the attributed string.

- `dict` — An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes

## Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## See Also

### Creating from HTML

- [- initWithHTML:baseURL:documentAttributes:](<init(html_baseurl_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object and base URL.
- [- initWithHTML:options:documentAttributes:](<init(html_options_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object.
- [+ loadFromHTMLWithRequest:options:completionHandler:](<loadfromhtml(request_options_completionhandler_).md>) — Creates an attributed string by converting the contents of the specified HTML URL request.
- [+ loadFromHTMLWithFileURL:options:completionHandler:](<loadfromhtml(fileurl_options_completionhandler_).md>) — Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [+ loadFromHTMLWithString:options:completionHandler:](<loadfromhtml(string_options_completionhandler_).md>) — Creates an attributed string from the specified HTML string.
- [+ loadFromHTMLWithData:options:completionHandler:](<loadfromhtml(data_options_completionhandler_).md>) — Creates an attributed string from the specified HTML data.
- [CompletionHandler](completionhandler.md) — A completion handler for getting an asynchronous attributed string.

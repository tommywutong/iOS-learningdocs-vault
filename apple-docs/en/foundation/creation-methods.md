---
title: Creation methods
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/creation-methods
source_url: 'https://developer.apple.com/documentation/foundation/creation-methods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/creation-methods.json'
content_hash: 'sha256:c61b55e51cecd773'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSAttributedString](nsattributedstring.md)

# Creation methods

<sub>API Collection</sub>

Create attributed strings from existing content or raw text and apply the initial attributes.

## Topics

### Creating from another string

- [- initWithString:](<nsattributedstring/init(string_).md>) — Creates an attributed string with the specified text and no attribute information.
- [- initWithString:attributes:](<nsattributedstring/init(string_attributes_).md>) — Creates an attributed string with the specified text and attributes.
- [- initWithAttributedString:](<nsattributedstring/init(attributedstring_).md>) — Creates a new attributed string from the contents of another attributed string.

### Creating a formatted string

- [init(_:)](<nsattributedstring/init(__).md>) — Creates a reference-type attributed string from the specified value-type attributed string.
- [init(_:including:)](<nsattributedstring/init(__including_)-9gogq.md>) — Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.
- [init(_:including:)](<nsattributedstring/init(__including_)-8iy4i.md>) — Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.

### Creating from a data file

- [- initWithData:options:documentAttributes:error:](<nsattributedstring/init(data_options_documentattributes_).md>) — Creates an attributed string from the contents of the specified data object.
- [- initWithDocFormat:documentAttributes:](<nsattributedstring/init(docformat_documentattributes_).md>) — Creates an attributed string from Microsoft Word format data in the specified data object.
- [- initWithURL:options:documentAttributes:error:](<nsattributedstring/init(url_options_documentattributes_).md>) — Creates an attributed string from the contents of the specified URL.

### Creating from HTML

- [- initWithHTML:documentAttributes:](<nsattributedstring/init(html_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object.
- [- initWithHTML:baseURL:documentAttributes:](<nsattributedstring/init(html_baseurl_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object and base URL.
- [- initWithHTML:options:documentAttributes:](<nsattributedstring/init(html_options_documentattributes_).md>) — Creates an attributed string from the HTML in the specified data object.
- [+ loadFromHTMLWithRequest:options:completionHandler:](<nsattributedstring/loadfromhtml(request_options_completionhandler_).md>) — Creates an attributed string by converting the contents of the specified HTML URL request.
- [+ loadFromHTMLWithFileURL:options:completionHandler:](<nsattributedstring/loadfromhtml(fileurl_options_completionhandler_).md>) — Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [+ loadFromHTMLWithString:options:completionHandler:](<nsattributedstring/loadfromhtml(string_options_completionhandler_).md>) — Creates an attributed string from the specified HTML string.
- [+ loadFromHTMLWithData:options:completionHandler:](<nsattributedstring/loadfromhtml(data_options_completionhandler_).md>) — Creates an attributed string from the specified HTML data.
- [CompletionHandler](nsattributedstring/completionhandler.md) — A completion handler for getting an asynchronous attributed string.

### Creating from RTF

- [- initWithRTF:documentAttributes:](<nsattributedstring/init(rtf_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [- initWithRTFD:documentAttributes:](<nsattributedstring/init(rtfd_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.
- [- initWithRTFDFileWrapper:documentAttributes:](<nsattributedstring/init(rtfdfilewrapper_documentattributes_).md>) — Creates an attributed string from the specified file wrapper that contains an RTFD document.

### Creating from markdown

- [init(markdown:options:baseURL:)](<nsattributedstring/init(markdown_options_baseurl_)-m9n.md>) — Creates an attributed string from a Markdown-formatted string using the provided options.
- [init(markdown:options:baseURL:)](<nsattributedstring/init(markdown_options_baseurl_)-5nru2.md>) — Creates an attributed string from Markdown-formatted data using the provided options.
- [init(contentsOf:options:baseURL:)](<nsattributedstring/init(contentsof_options_baseurl_).md>) — Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.

### Creating a string with an attachment

- [+ attributedStringWithAttachment:](<nsattributedstring/init(attachment_).md>) — Creates an attributed string with an attachment.
- [+ attributedStringWithAttachment:attributes:](<nsattributedstring/init(attachment_attributes_).md>) — Creates an attributed string with an attachment and applies the specified attributes to it.
- [+ attributedStringWithAdaptiveImageGlyph:attributes:](<nsattributedstring/init(adaptiveimageglyph_attributes_).md>) — Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.

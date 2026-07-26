---
title: 'initWithMarkdown:options:baseURL:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/initwithmarkdown:options:baseurl:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/initwithmarkdown:options:baseurl:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/initwithmarkdown%3Aoptions%3Abaseurl%3Aerror%3A.json'
content_hash: 'sha256:0afa0275f124ad7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# initWithMarkdown:options:baseURL:error:

<sub>Instance Method</sub>

Creates an attributed string from Markdown-formatted data using the provided options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithMarkdown:(NSData *) markdown options:(NSAttributedStringMarkdownParsingOptions *) options baseURL:(NSURL *) baseURL error:(NSError **) error;
```

## Parameters

- `markdown` — The [NSData](../nsdata.md) instance that contains the Markdown formatting.

- `options` — Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.

- `baseURL` — The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is `nil`, the initializer doesn’t resolve URLs. The default is `nil`.

- `error` — On input, a pointer to an error object. On return, if an error occurs, this pointer contains an actual error object with the error information. You may specify `nil` for this parameter if you don’t want the error information.

## Return Value

An attributed string with the parsed Markdown text and styling, or `nil` if parsing the data fails.

## See Also

### Creating from markdown

- [initWithMarkdownString:options:baseURL:error:](initwithmarkdownstring_options_baseurl_error_.md) — Creates an attributed string from a Markdown-formatted string using the provided options.
- [initWithContentsOfMarkdownFileAtURL:options:baseURL:error:](initwithcontentsofmarkdownfileaturl_options_baseurl_error_.md) — Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.
- [NSAttributedStringMarkdownParsingOptions](../nsattributedstringmarkdownparsingoptions.md) — Options that affect the parsing of Markdown content into an attributed string.

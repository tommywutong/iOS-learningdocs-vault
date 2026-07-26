---
title: 'init(contentsOf:options:baseURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(contentsof:options:baseurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(contentsof:options:baseurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28contentsof%3Aoptions%3Abaseurl%3A%29.json'
content_hash: 'sha256:4e50397e1d3ad4a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(contentsOf:options:baseURL:)

<sub>Initializer</sub>

Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(contentsOf url: URL, options: AttributedString.MarkdownParsingOptions = .init(), baseURL: URL? = nil) throws
```

## Parameters

- `url` — The URL to load Markdown-formatted data from.

- `options` — Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.

- `baseURL` — The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is `nil`, the initializer doesn’t resolve URLs. The default is `nil`.

## See Also

### Creating from markdown

- [init(markdown:options:baseURL:)](<init(markdown_options_baseurl_)-m9n.md>) — Creates an attributed string from a Markdown-formatted string using the provided options.
- [init(markdown:options:baseURL:)](<init(markdown_options_baseurl_)-5nru2.md>) — Creates an attributed string from Markdown-formatted data using the provided options.

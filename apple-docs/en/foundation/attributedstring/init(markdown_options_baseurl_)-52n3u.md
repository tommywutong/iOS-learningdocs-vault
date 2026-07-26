---
title: 'init(markdown:options:baseURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(markdown:options:baseurl:)-52n3u'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(markdown:options:baseurl:)-52n3u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28markdown%3Aoptions%3Abaseurl%3A%29-52n3u.json'
content_hash: 'sha256:dae46f9afe1c32b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(markdown:options:baseURL:)

<sub>Initializer</sub>

Creates an attributed string from a Markdown-formatted string using the provided options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(markdown: String, options: AttributedString.MarkdownParsingOptions = .init(), baseURL: URL? = nil) throws
```

## Parameters

- `markdown` — The string that contains the Markdown formatting.

- `options` — Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.

- `baseURL` — The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is `nil`, the initializer doesn’t resolve URLs. The default is `nil`.

## Discussion

If your source string includes custom attributes defined by conformers to [MarkdownDecodableAttributedStringKey](../markdowndecodableattributedstringkey.md) and used with Apple’s markdown extension syntax, be sure to include the [allowsExtendedAttributes](../nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) option. Otherwise, the initializer doesn’t parse these attributes.

## See Also

### Initializing from Markdown Strings

- [init(markdown:including:options:baseURL:)](<init(markdown_including_options_baseurl_)-4m51b.md>) — Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope.
- [init(markdown:including:options:baseURL:)](<init(markdown_including_options_baseurl_)-89e48.md>) — Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope that a key path identifies.

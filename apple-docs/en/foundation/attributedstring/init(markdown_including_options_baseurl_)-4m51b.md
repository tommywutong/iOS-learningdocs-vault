---
title: 'init(markdown:including:options:baseURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(markdown:including:options:baseurl:)-4m51b'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(markdown:including:options:baseurl:)-4m51b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28markdown%3Aincluding%3Aoptions%3Abaseurl%3A%29-4m51b.json'
content_hash: 'sha256:8a0215d59f68de00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(markdown:including:options:baseURL:)

<sub>Initializer</sub>

Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(markdown: String, including scope: S.Type, options: AttributedString.MarkdownParsingOptions = .init(), baseURL: URL? = nil) throws where S : AttributeScope
```

## Parameters

- `markdown` — The string that contains the Markdown formatting.

- `scope` — The attribute scope to associate with the attributed string.

- `options` — Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.

- `baseURL` — The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is `nil`, the initializer doesn’t resolve URLs. The default is `nil`.

## Discussion

If your source string includes custom attributes defined by conformers to [MarkdownDecodableAttributedStringKey](../markdowndecodableattributedstringkey.md) and used with Apple’s markdown extension syntax, be sure to include the [allowsExtendedAttributes](../nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) option. Otherwise, the initializer doesn’t parse these attributes.

## See Also

### Initializing from Markdown Strings

- [init(markdown:options:baseURL:)](<init(markdown_options_baseurl_)-52n3u.md>) — Creates an attributed string from a Markdown-formatted string using the provided options.
- [init(markdown:including:options:baseURL:)](<init(markdown_including_options_baseurl_)-89e48.md>) — Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope that a key path identifies.

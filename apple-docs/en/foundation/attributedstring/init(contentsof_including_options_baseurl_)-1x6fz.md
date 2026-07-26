---
title: 'init(contentsOf:including:options:baseURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(contentsof:including:options:baseurl:)-1x6fz'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(contentsof:including:options:baseurl:)-1x6fz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28contentsof%3Aincluding%3Aoptions%3Abaseurl%3A%29-1x6fz.json'
content_hash: 'sha256:1fd7fc468c8692fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(contentsOf:including:options:baseURL:)

<sub>Initializer</sub>

Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data, using the provided options and attribute scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(contentsOf url: URL, including scope: S.Type, options: AttributedString.MarkdownParsingOptions = .init(), baseURL: URL? = nil) throws where S : AttributeScope
```

## Parameters

- `url` — The URL to load Markdown-formatted data from.

- `scope` — An attribute scope to associate with the attributed string.

- `options` — Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.

- `baseURL` — The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is `nil`, the initializer doesn’t resolve URLs. The default is `nil`.

## Discussion

If your source string includes custom attributes defined by conformers to [MarkdownDecodableAttributedStringKey](../markdowndecodableattributedstringkey.md) and used with Apple’s markdown extension syntax, be sure to include the [allowsExtendedAttributes](../nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) option. Otherwise, the initializer doesn’t parse these attributes.

## See Also

### Initializing with Markdown from URL Contents

- [init(contentsOf:options:baseURL:)](<init(contentsof_options_baseurl_).md>) — Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data, using the provided options.
- [init(contentsOf:including:options:baseURL:)](<init(contentsof_including_options_baseurl_)-1fcpy.md>) — Creates an attributed string from the contents of a specified Markdown URL, using the provided options and attribute scope that a key path identifies.

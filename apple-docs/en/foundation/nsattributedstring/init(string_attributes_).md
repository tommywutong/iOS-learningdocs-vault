---
title: 'init(string:attributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(string:attributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(string:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28string%3Aattributes%3A%29.json'
content_hash: 'sha256:b991bc761b814047'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(string:attributes:)

<sub>Initializer</sub>

Creates an attributed string with the specified text and attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(string str: String, attributes attrs: [NSAttributedString.Key : Any]? = nil)
```

## Parameters

- `str` — The text for the new attributed string.

- `attrs` — The attributes for the new attributed string. This method applies the attributes to the entire string. For a list of attributes that you can include in this dictionary, see [Key](key.md).

## Discussion

Returns an [NSAttributedString](../nsattributedstring.md) object initialized with the characters of `str` and the attributes of `attrs`.

## See Also

### Related Documentation

- [- initWithRTF:documentAttributes:](<init(rtf_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.

### Creating from another string

- [- initWithString:](<init(string_).md>) — Creates an attributed string with the specified text and no attribute information.
- [- initWithAttributedString:](<init(attributedstring_).md>) — Creates a new attributed string from the contents of another attributed string.

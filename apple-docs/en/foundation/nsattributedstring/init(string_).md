---
title: 'init(string:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(string:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(string:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28string%3A%29.json'
content_hash: 'sha256:081f4f749ce4c64d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(string:)

<sub>Initializer</sub>

Creates an attributed string with the specified text and no attribute information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(string str: String)
```

## Parameters

- `str` — The text for the new attributed string.

## Return Value

An [NSAttributedString](../nsattributedstring.md) object initialized with the characters of `str` and no attribute information.

## See Also

### Related Documentation

- [- initWithRTF:documentAttributes:](<init(rtf_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [Attributed String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/AttributedStrings.html#//apple_ref/doc/uid/10000036i)

### Creating from another string

- [- initWithString:attributes:](<init(string_attributes_).md>) — Creates an attributed string with the specified text and attributes.
- [- initWithAttributedString:](<init(attributedstring_).md>) — Creates a new attributed string from the contents of another attributed string.

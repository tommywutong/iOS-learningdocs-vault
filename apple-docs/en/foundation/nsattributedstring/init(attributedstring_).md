---
title: 'init(attributedString:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(attributedstring:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(attributedstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28attributedstring%3A%29.json'
content_hash: 'sha256:88309249ae4d71a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(attributedString:)

<sub>Initializer</sub>

Creates a new attributed string from the contents of another attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(attributedString attrStr: NSAttributedString)
```

## Parameters

- `attrStr` — An attributed string.

## Return Value

An [NSAttributedString](../nsattributedstring.md) object initialized with the characters and attributes of `attrStr`.

## See Also

### Related Documentation

- [- initWithRTF:documentAttributes:](<init(rtf_documentattributes_).md>) — Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.

### Creating from another string

- [- initWithString:](<init(string_).md>) — Creates an attributed string with the specified text and no attribute information.
- [- initWithString:attributes:](<init(string_attributes_).md>) — Creates an attributed string with the specified text and attributes.

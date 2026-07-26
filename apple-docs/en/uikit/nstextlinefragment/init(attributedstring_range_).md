---
title: 'init(attributedString:range:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlinefragment/init(attributedstring:range:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment/init(attributedstring:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment/init%28attributedstring%3Arange%3A%29.json'
content_hash: 'sha256:1bf89001f4a1051d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLineFragment](../nstextlinefragment.md)

# init(attributedString:range:)

<sub>Initializer</sub>

Creates a new line fragment from the attributed string for the range of characters you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(attributedString: NSAttributedString, range: NSRange)
```

## Parameters

- `attributedString` — The attributed string.

- `range` — An [NSRange](../../foundation/nsrange-c.struct.md) that specifies which characters to include.

## See Also

### Creating line fragments

- [- initWithCoder:](<init(coder_).md>) — Creates a new line fragment with from data in an unarchiver.
- [- initWithString:attributes:range:](<init(string_attributes_range_).md>) — Creates a new line fragment using the string, attributes, and range you provide.

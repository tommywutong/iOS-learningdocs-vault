---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlinefragment/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment/init%28coder%3A%29.json'
content_hash: 'sha256:1dc640e719ee2d03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLineFragment](../nstextlinefragment.md)

# init(coder:)

<sub>Initializer</sub>

Creates a new line fragment with from data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder aDecoder: NSCoder)
```

## Parameters

- `aDecoder` — A decoder that conforms to the [NSCoder](../../foundation/nscoder.md) protocol.

## See Also

### Creating line fragments

- [- initWithAttributedString:range:](<init(attributedstring_range_).md>) — Creates a new line fragment from the attributed string for the range of characters you specify.
- [- initWithString:attributes:range:](<init(string_attributes_range_).md>) — Creates a new line fragment using the string, attributes, and range you provide.

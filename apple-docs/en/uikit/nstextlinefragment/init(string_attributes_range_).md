---
title: 'init(string:attributes:range:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlinefragment/init(string:attributes:range:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment/init(string:attributes:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment/init%28string%3Aattributes%3Arange%3A%29.json'
content_hash: 'sha256:f1b1d05179506148'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLineFragment](../nstextlinefragment.md)

# init(string:attributes:range:)

<sub>Initializer</sub>

Creates a new line fragment using the string, attributes, and range you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(string: String, attributes: [NSAttributedString.Key : Any] = [:], range: NSRange)
```

## Parameters

- `string` — An attributed string.

- `attributes` — A dictionary of attributes.

- `range` — The range to use from `string`.

## See Also

### Creating line fragments

- [- initWithAttributedString:range:](<init(attributedstring_range_).md>) — Creates a new line fragment from the attributed string for the range of characters you specify.
- [- initWithCoder:](<init(coder_).md>) — Creates a new line fragment with from data in an unarchiver.

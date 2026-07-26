---
title: 'init(text:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisimpletextprintformatter/init(text:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/init(text:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisimpletextprintformatter/init%28text%3A%29.json'
content_hash: 'sha256:3e3b863e07284e72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md)

# init(text:)

<sub>Initializer</sub>

Returns a simple-text print formatter initialized with plain text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(text: String)
```

## Parameters

- `text` — A string of plain text or `nil` if you intend to assign the text later.

## Return Value

An initialized instance of `UISimpleTextPrintFormatter` or `nil` if the object could not be created.

## See Also

### Related Documentation

- [text](text.md) — A string of plain text.

### Creating a simple-text print formatter

- [- initWithAttributedText:](<init(attributedtext_).md>) — Returns a simple-text print formatter initialized with attributed text.

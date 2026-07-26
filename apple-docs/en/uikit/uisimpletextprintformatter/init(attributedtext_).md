---
title: 'init(attributedText:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisimpletextprintformatter/init(attributedtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/init(attributedtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisimpletextprintformatter/init%28attributedtext%3A%29.json'
content_hash: 'sha256:75279ba37364d2cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md)

# init(attributedText:)

<sub>Initializer</sub>

Returns a simple-text print formatter initialized with attributed text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(attributedText: NSAttributedString)
```

## Parameters

- `attributedText` — A string of attributed text or `nil` if you intend to assign the text later.

## Return Value

An initialized instance of `UISimpleTextPrintFormatter` or `nil` if the object could not be created.

## See Also

### Related Documentation

- [attributedText](attributedtext.md) — A string of attributed text.

### Creating a simple-text print formatter

- [- initWithText:](<init(text_).md>) — Returns a simple-text print formatter initialized with plain text.

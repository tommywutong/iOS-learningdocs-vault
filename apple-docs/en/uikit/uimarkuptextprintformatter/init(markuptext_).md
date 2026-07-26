---
title: 'init(markupText:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimarkuptextprintformatter/init(markuptext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/init(markuptext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimarkuptextprintformatter/init%28markuptext%3A%29.json'
content_hash: 'sha256:9a5233246b40a72c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMarkupTextPrintFormatter](../uimarkuptextprintformatter.md)

# init(markupText:)

<sub>Initializer</sub>

Returns a markup-text print formatter initialized with an HTML string.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(markupText: String)
```

## Parameters

- `markupText` — A string of HTML markup text or `nil` if you want to add the markup text later.

## Return Value

An instance of `UIMarkupTextPrintFormatter` or `nil` if the object could not be created.

## See Also

### Related Documentation

- [markupText](markuptext.md) — The HTML markup text for the print formatter.

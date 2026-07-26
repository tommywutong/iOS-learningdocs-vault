---
title: 'textScale(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/textscale(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/textscale(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/textscale%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:565ac5ab6bcc7c32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# textScale(_:isEnabled:)

<sub>Instance Method</sub>

Applies a text scale to the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func textScale(_ scale: Text.Scale, isEnabled: Bool = true) -> Text
```

## Parameters

- `scale` — The text scale to apply.

- `isEnabled` — If true the text scale is applied; otherwise text scale is unchanged.

## Return Value

Text with the specified scale applied.

## See Also

### Fitting text into available space

- [Scale](scale.md) — Defines text scales
- [TruncationMode](truncationmode.md) — The type of truncation to apply to a line of text when it’s too long to fit in the available space.

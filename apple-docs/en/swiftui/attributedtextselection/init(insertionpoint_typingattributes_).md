---
title: 'init(insertionPoint:typingAttributes:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextselection/init(insertionpoint:typingattributes:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextselection/init(insertionpoint:typingattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextselection/init%28insertionpoint%3Atypingattributes%3A%29.json'
content_hash: 'sha256:d1b7b57338aadb3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextSelection](../attributedtextselection.md)

# init(insertionPoint:typingAttributes:)

<sub>Initializer</sub>

Initialize a selection to a single insertion point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(insertionPoint: AttributedString.Index, typingAttributes: AttributeContainer? = nil)
```

## Parameters

- `insertionPoint` — The index of the string where the charet should be positioned.

- `typingAttributes` — The attributes for the next character that is typed, or `nil` if they should be inferred from the attributes on the text.

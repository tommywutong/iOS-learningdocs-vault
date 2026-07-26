---
title: 'typingAttributes(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextselection/typingattributes(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextselection/typingattributes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextselection/typingattributes%28in%3A%29.json'
content_hash: 'sha256:91615b4d4575e5ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextSelection](../attributedtextselection.md)

# typingAttributes(in:)

<sub>Instance Method</sub>

Returns the typing attributes for a corresponding text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func typingAttributes(in text: AttributedString) -> AttributeContainer
```

## Discussion

The typing attributes are the attributes that will be applied to any new characters typed out by the user.

> [!note] Note
> The returned container may contain values for attributes that specify [runBoundaries](../../foundation/attributedstringkey/runboundaries.md) and thus might not actually get applied to new content.

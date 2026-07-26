---
title: 'sizeThatFits(proposal:text:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textrenderer/sizethatfits(proposal:text:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textrenderer/sizethatfits(proposal:text:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textrenderer/sizethatfits%28proposal%3Atext%3A%29.json'
content_hash: 'sha256:fcf33390eaa1880e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextRenderer](../textrenderer.md)

# sizeThatFits(proposal:text:)

<sub>Instance Method</sub>

Returns the size of the text in `proposal`. The provided `text` proxy value may be used to query the sizing behavior of the underlying text layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sizeThatFits(proposal: ProposedViewSize, text: TextProxy) -> CGSize
```

## Discussion

The default implementation of this function returns `text.size(proposal)`.

## Default Implementations

### TextRenderer Implementations

- [sizeThatFits(proposal:text:)](<sizethatfits(proposal_text_)-3wr9v.md>) — Returns the size of the text in `proposal`. The provided `text` proxy value may be used to query the sizing behavior of the underlying text layout.

---
title: 'sizeThatFits(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textproxy/sizethatfits(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textproxy/sizethatfits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textproxy/sizethatfits%28_%3A%29.json'
content_hash: 'sha256:bde833f12fffd847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextProxy](../textproxy.md)

# sizeThatFits(_:)

<sub>Instance Method</sub>

Returns the space needed by the text view, for a proposed size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize
```

## Parameters

- `proposal` — The proposed size of the text view.

## Return Value

The size that the text view requires for the given proposal.

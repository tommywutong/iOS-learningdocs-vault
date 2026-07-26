---
title: leadingFirstTextBaseline
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alignment/leadingfirsttextbaseline
source_url: 'https://developer.apple.com/documentation/swiftui/alignment/leadingfirsttextbaseline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alignment/leadingfirsttextbaseline.json'
content_hash: 'sha256:1de118f8691fa6c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alignment](../alignment.md)

# leadingFirstTextBaseline

<sub>Type Property</sub>

A guide that marks the leading edge and top-most text baseline in a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var leadingFirstTextBaseline: Alignment { get }
```

## Discussion

This alignment combines the [leading](../horizontalalignment/leading.md) horizontal guide and the [firstTextBaseline](../verticalalignment/firsttextbaseline.md) vertical guide:

![A square that’s divided into four equal quadrants. The upper-](../../../../attachments/fb626b3fdb3acf7b14e4279080b077f6/Alignment-leadingFirstTextBaseline-1-iOS@2x.png)

## See Also

### Getting text baseline guides

- [centerFirstTextBaseline](centerfirsttextbaseline.md) — A guide that marks the top-most text baseline in a view.
- [trailingFirstTextBaseline](trailingfirsttextbaseline.md) — A guide that marks the trailing edge and top-most text baseline in a view.
- [leadingLastTextBaseline](leadinglasttextbaseline.md) — A guide that marks the leading edge and bottom-most text baseline in a view.
- [centerLastTextBaseline](centerlasttextbaseline.md) — A guide that marks the bottom-most text baseline in a view.
- [trailingLastTextBaseline](trailinglasttextbaseline.md) — A guide that marks the trailing edge and bottom-most text baseline in a view.

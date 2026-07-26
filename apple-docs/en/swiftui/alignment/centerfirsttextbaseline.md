---
title: centerFirstTextBaseline
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alignment/centerfirsttextbaseline
source_url: 'https://developer.apple.com/documentation/swiftui/alignment/centerfirsttextbaseline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alignment/centerfirsttextbaseline.json'
content_hash: 'sha256:1f3d1786ebd42942'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alignment](../alignment.md)

# centerFirstTextBaseline

<sub>Type Property</sub>

A guide that marks the top-most text baseline in a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var centerFirstTextBaseline: Alignment { get }
```

## Discussion

This alignment combines the [center](../horizontalalignment/center.md) horizontal guide and the [firstTextBaseline](../verticalalignment/firsttextbaseline.md) vertical guide:

![A square that’s divided into four equal quadrants. The upper-](../../../../attachments/678f6786ba0bc12846f4c13d3a41702e/Alignment-centerFirstTextBaseline-1-iOS@2x.png)

## See Also

### Getting text baseline guides

- [leadingFirstTextBaseline](leadingfirsttextbaseline.md) — A guide that marks the leading edge and top-most text baseline in a view.
- [trailingFirstTextBaseline](trailingfirsttextbaseline.md) — A guide that marks the trailing edge and top-most text baseline in a view.
- [leadingLastTextBaseline](leadinglasttextbaseline.md) — A guide that marks the leading edge and bottom-most text baseline in a view.
- [centerLastTextBaseline](centerlasttextbaseline.md) — A guide that marks the bottom-most text baseline in a view.
- [trailingLastTextBaseline](trailinglasttextbaseline.md) — A guide that marks the trailing edge and bottom-most text baseline in a view.

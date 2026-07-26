---
title: centerLastTextBaseline
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alignment/centerlasttextbaseline
source_url: 'https://developer.apple.com/documentation/swiftui/alignment/centerlasttextbaseline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alignment/centerlasttextbaseline.json'
content_hash: 'sha256:124dfad99305dfc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alignment](../alignment.md)

# centerLastTextBaseline

<sub>Type Property</sub>

A guide that marks the bottom-most text baseline in a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var centerLastTextBaseline: Alignment { get }
```

## Discussion

This alignment combines the [center](../horizontalalignment/center.md) horizontal guide and the [lastTextBaseline](../verticalalignment/lasttextbaseline.md) vertical guide:

![A square that’s divided into four equal quadrants. The upper-](../../../../attachments/721a60b87f43a3e8cd5342720b6b0770/Alignment-centerLastTextBaseline-1-iOS@2x.png)

## See Also

### Getting text baseline guides

- [leadingFirstTextBaseline](leadingfirsttextbaseline.md) — A guide that marks the leading edge and top-most text baseline in a view.
- [centerFirstTextBaseline](centerfirsttextbaseline.md) — A guide that marks the top-most text baseline in a view.
- [trailingFirstTextBaseline](trailingfirsttextbaseline.md) — A guide that marks the trailing edge and top-most text baseline in a view.
- [leadingLastTextBaseline](leadinglasttextbaseline.md) — A guide that marks the leading edge and bottom-most text baseline in a view.
- [trailingLastTextBaseline](trailinglasttextbaseline.md) — A guide that marks the trailing edge and bottom-most text baseline in a view.

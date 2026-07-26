---
title: top
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/alignment-swift.enum/top
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.enum/top'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/alignment-swift.enum/top.json'
content_hash: 'sha256:345630209f67a345'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIStackView](../../uistackview.md) · [Alignment](../alignment-swift.enum.md)

# top

<sub>Type Property</sub>

A layout for horizontal stacks where the stack view aligns the top edge of its arranged views along its top edge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var top: UIStackView.Alignment { get }
```

## Discussion

This value is equivalent to the [UIStackViewAlignmentLeading](leading.md) alignment for vertical stacks.

The following image shows an example of a horizontal stack view that uses the [UIStackViewAlignmentTop](top.md) alignment.

![A horizontal stack view with four arranged subviews. The stack view aligns the subviews to its top edge.](../../../../../attachments/ac8be4305f320bb371d4f5981fdc2cfb/media-2557465@2x.png)

## See Also

### Constants

- [UIStackViewAlignmentFill](fill.md) — A layout where the stack view resizes its arranged views so that they fill the available space perpendicular to the stack view’s axis.
- [UIStackViewAlignmentCenter](center.md) — A layout where the stack view aligns the center of its arranged views with its center along its axis.
- [UIStackViewAlignmentLeading](leading.md) — A layout for vertical stacks where the stack view aligns the leading edge of its arranged views along its leading edge.
- [UIStackViewAlignmentTrailing](trailing.md) — A layout for vertical stacks where the stack view aligns the trailing edge of its arranged views along its trailing edge.
- [UIStackViewAlignmentBottom](bottom.md) — A layout for horizontal stacks where the stack view aligns the bottom edge of its arranged views along its bottom edge.
- [UIStackViewAlignmentFirstBaseline](firstbaseline.md) — A layout for horizontal stacks where the stack view aligns its arranged views based on their first baseline.
- [UIStackViewAlignmentLastBaseline](lastbaseline.md) — A layout for horizontal stacks where the stack view aligns its arranged views based on their last baseline.

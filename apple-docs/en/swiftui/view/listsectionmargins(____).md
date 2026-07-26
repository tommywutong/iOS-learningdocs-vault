---
title: 'listSectionMargins(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listsectionmargins(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listsectionmargins(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listsectionmargins%28_%3A_%3A%29.json'
content_hash: 'sha256:1a7657ae17ade9bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listSectionMargins(_:_:)

<sub>Instance Method</sub>

Set the section margins for the specific edges.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func listSectionMargins(_ edges: Edge.Set = .all, _ length: CGFloat?) -> some View

```

## Parameters

- `edges` — The set of edges to pad for sections in this view. The default is [all](../edge/set/all.md).

- `length` — An amount, given in points, to pad section on the specified edges.

## Return Value

A view in which the margins of list sections are set to the specified amount on the specified edges.

## Discussion

Use this modifier on a list section to set customize its margins. Indicate the edges to set the margin of by naming either a single value from  [Set](../edge/set.md), or by specifying an [OptionSet](../../swift/optionset.md) that contains edge values. Margins for the other edges remain unchanged.

The default section margins are based on the list style, list section spacing and content margins of the list. Using this modifier overrides these default values completely.

For sections that have headers or footers, the section margins are applied around these.

## See Also

### Configuring a list’s layout

- [listRowInsets(_:)](<listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [listRowInsets(_:_:)](<listrowinsets(____).md>) — Sets the insets of rows in a list on the specified edges.
- [defaultMinListRowHeight](../environmentvalues/defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [defaultMinListHeaderHeight](../environmentvalues/defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [listRowSpacing(_:)](<listrowspacing(__).md>) — Sets the vertical spacing between two adjacent rows in a List.
- [listSectionSpacing(_:)](<listsectionspacing(__).md>) — Sets the spacing between adjacent sections in a [List](../list.md) to a custom value.
- [ListSectionSpacing](../listsectionspacing.md) — The spacing options between two adjacent sections in a list.

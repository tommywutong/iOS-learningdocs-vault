---
title: defaultMinListRowHeight
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/defaultminlistrowheight
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/defaultminlistrowheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/defaultminlistrowheight.json'
content_hash: 'sha256:b53f12bc444a7e3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# defaultMinListRowHeight

<sub>Instance Property</sub>

The default minimum height of rows in a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var defaultMinListRowHeight: CGFloat { get set }
```

## Discussion

The height of list rows is bounded below by this default value, and is otherwise determined by the height of the row’s content and the row insets.

## See Also

### Configuring a list’s layout

- [listRowInsets(_:)](<../view/listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [listRowInsets(_:_:)](<../view/listrowinsets(____).md>) — Sets the insets of rows in a list on the specified edges.
- [defaultMinListHeaderHeight](defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [listRowSpacing(_:)](<../view/listrowspacing(__).md>) — Sets the vertical spacing between two adjacent rows in a List.
- [listSectionSpacing(_:)](<../view/listsectionspacing(__).md>) — Sets the spacing between adjacent sections in a [List](../list.md) to a custom value.
- [ListSectionSpacing](../listsectionspacing.md) — The spacing options between two adjacent sections in a list.
- [listSectionMargins(_:_:)](<../view/listsectionmargins(____).md>) — Set the section margins for the specific edges.

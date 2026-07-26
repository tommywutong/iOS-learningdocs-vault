---
title: defaultMinListHeaderHeight
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/defaultminlistheaderheight
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/defaultminlistheaderheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/defaultminlistheaderheight.json'
content_hash: 'sha256:bc56fcae2384279c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# defaultMinListHeaderHeight

<sub>Instance Property</sub>

The default minimum height of a header in a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var defaultMinListHeaderHeight: CGFloat? { get set }
```

## Discussion

When this value is `nil`, the system chooses the appropriate height. The default is `nil`.

## See Also

### Configuring a list’s layout

- [listRowInsets(_:)](<../view/listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [listRowInsets(_:_:)](<../view/listrowinsets(____).md>) — Sets the insets of rows in a list on the specified edges.
- [defaultMinListRowHeight](defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [listRowSpacing(_:)](<../view/listrowspacing(__).md>) — Sets the vertical spacing between two adjacent rows in a List.
- [listSectionSpacing(_:)](<../view/listsectionspacing(__).md>) — Sets the spacing between adjacent sections in a [List](../list.md) to a custom value.
- [ListSectionSpacing](../listsectionspacing.md) — The spacing options between two adjacent sections in a list.
- [listSectionMargins(_:_:)](<../view/listsectionmargins(____).md>) — Set the section margins for the specific edges.

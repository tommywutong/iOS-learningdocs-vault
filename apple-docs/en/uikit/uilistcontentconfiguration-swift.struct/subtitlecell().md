---
title: subtitleCell()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/subtitlecell()
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/subtitlecell()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/subtitlecell%28%29.json'
content_hash: 'sha256:5ef06184bcefbdb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# subtitleCell()

<sub>Type Method</sub>

Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func subtitleCell() -> UIListContentConfiguration
```

## Return Value

The default configuration for a cell that’s in a list and contains subtitle text.

## Discussion

Create this configuration to update the content and styling of a cell in a list. When you apply this configuration to a cell, the cell displays one primary label and one subtitle label below the primary label. Both labels resize automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in a table view or collection view list that you configure with one of the following enumeration cases:

- [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md)
- [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md)
- [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md)
- [UICollectionLayoutListConfiguration.Appearance.plain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md)
- [UICollectionLayoutListConfiguration.Appearance.grouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md)
- [UICollectionLayoutListConfiguration.Appearance.insetGrouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md)

Configure the background of your cell using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listPlainCell()](<../uibackgroundconfiguration-swift.struct/listplaincell().md>) | [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md), [UICollectionLayoutListConfiguration.Appearance.plain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) |
| [listGroupedCell()](<../uibackgroundconfiguration-swift.struct/listgroupedcell().md>) | [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md), [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md), [UICollectionLayoutListConfiguration.Appearance.grouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md), [UICollectionLayoutListConfiguration.Appearance.insetGrouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md) |

## See Also

### Creating default cell configurations

- [cell()](<cell().md>) — Creates the default configuration you use to style a cell in a list.
- [valueCell()](<valuecell().md>) — Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [sidebarCell()](<sidebarcell().md>) — Creates the default configuration you use to style a cell in a sidebar list.
- [sidebarSubtitleCell()](<sidebarsubtitlecell().md>) — Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.
- [accompaniedSidebarCell()](<accompaniedsidebarcell().md>) — Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [accompaniedSidebarSubtitleCell()](<accompaniedsidebarsubtitlecell().md>) — Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.

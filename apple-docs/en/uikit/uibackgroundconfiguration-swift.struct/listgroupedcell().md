---
title: listGroupedCell()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-swift.struct/listgroupedcell()
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listgroupedcell()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-swift.struct/listgroupedcell%28%29.json'
content_hash: 'sha256:eb01cff926419407'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md)

# listGroupedCell()

<sub>Type Method</sub>

Creates the default configuration you use to style a cell in a grouped list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func listGroupedCell() -> UIBackgroundConfiguration
```

## Return Value

The default configuration for a cell in a grouped list.

## Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a grouped cell, including styling for highlighted and selected states.

For an appearance consistent with system defaults, use this background configuration for a cell in these contexts:

- A table view that you configure with the [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md) or [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md) enumeration case.
- A collection view list that you configure with the [UICollectionLayoutListConfiguration.Appearance.grouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md) or [UICollectionLayoutListConfiguration.Appearance.insetGrouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md) enumeration case.

## See Also

### Creating cell background configurations

- [listPlainCell()](<listplaincell().md>) — Creates the default configuration you use to style a cell in a plain list.
- [listSidebarCell()](<listsidebarcell().md>) — Creates the default configuration you use to style a cell in a sidebar list.
- [listAccompaniedSidebarCell()](<listaccompaniedsidebarcell().md>) — Creates the default configuration you use to style a cell in an accompanied sidebar list.

---
title: listSidebarCell()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-swift.struct/listsidebarcell()
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listsidebarcell()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-swift.struct/listsidebarcell%28%29.json'
content_hash: 'sha256:8712628519f1b44e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md)

# listSidebarCell()

<sub>Type Method</sub>

Creates the default configuration you use to style a cell in a sidebar list.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func listSidebarCell() -> UIBackgroundConfiguration
```

## Return Value

The default configuration for a cell in a sidebar list.

## Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a cell in a sidebar collection view list, including styling for highlighted and selected states.

For an appearance consistent with system defaults, use this background configuration for a cell in a collection view list that you configure with the [UICollectionLayoutListConfiguration.Appearance.sidebar](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) or [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) enumeration case.

## See Also

### Creating cell background configurations

- [listPlainCell()](<listplaincell().md>) — Creates the default configuration you use to style a cell in a plain list.
- [listGroupedCell()](<listgroupedcell().md>) — Creates the default configuration you use to style a cell in a grouped list.
- [listAccompaniedSidebarCell()](<listaccompaniedsidebarcell().md>) — Creates the default configuration you use to style a cell in an accompanied sidebar list.

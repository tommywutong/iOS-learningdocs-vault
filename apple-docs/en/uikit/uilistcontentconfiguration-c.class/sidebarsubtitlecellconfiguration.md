---
title: sidebarSubtitleCellConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/sidebarsubtitlecellconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/sidebarsubtitlecellconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/sidebarsubtitlecellconfiguration.json'
content_hash: 'sha256:ae6052ebac33a287'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# sidebarSubtitleCellConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) sidebarSubtitleCellConfiguration;
```

## Return Value

The default configuration for a cell that’s in a sidebar list and contains subtitle text.

## Discussion

Create this configuration to update the content and styling of a cell in a sidebar collection view list. When you apply this configuration to a cell, the cell displays one primary label and one subtitle label below the primary label. Both labels resize automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in a sidebar collection view list that you configure with one of the following enumeration cases:

- [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md)
- [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md)

Configure the background of your cell using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listSidebarCellConfiguration](../uibackgroundconfiguration-c.class/listsidebarcellconfiguration.md) | [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md), [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) |

## See Also

### Creating default cell configurations

- [cellConfiguration](cellconfiguration.md) — Creates the default configuration you use to style a cell in a list.
- [subtitleCellConfiguration](subtitlecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [valueCellConfiguration](valuecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [sidebarCellConfiguration](sidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in a sidebar list. _(deprecated)_
- [accompaniedSidebarCellConfiguration](accompaniedsidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [accompaniedSidebarSubtitleCellConfiguration](accompaniedsidebarsubtitlecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.

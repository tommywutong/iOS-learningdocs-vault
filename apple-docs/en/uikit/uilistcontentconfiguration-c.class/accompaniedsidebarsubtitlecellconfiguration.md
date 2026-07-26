---
title: accompaniedSidebarSubtitleCellConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/accompaniedsidebarsubtitlecellconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/accompaniedsidebarsubtitlecellconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/accompaniedsidebarsubtitlecellconfiguration.json'
content_hash: 'sha256:39b302c998ee1e3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# accompaniedSidebarSubtitleCellConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) accompaniedSidebarSubtitleCellConfiguration;
```

## Return Value

The default configuration for a cell that’s in an accompanied sidebar list and contains subtitle text.

## Discussion

Create this configuration to update the content and styling of a cell in an accompanied sidebar collection view list, where the list is in the primary column of a split view controller, accompanied by another list in the split view controller’s supplementary column. When you apply this configuration to a cell, the cell displays one primary label and one subtitle label below the primary label. Both labels resize automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in an accompanied sidebar collection view list that you configure with one of the following enumeration cases:

- [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md)
- [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md)

Configure the background of your cell using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listAccompaniedSidebarCellConfiguration](../uibackgroundconfiguration-c.class/listaccompaniedsidebarcellconfiguration.md) | [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md), [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) |

## See Also

### Creating default cell configurations

- [cellConfiguration](cellconfiguration.md) — Creates the default configuration you use to style a cell in a list.
- [subtitleCellConfiguration](subtitlecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [valueCellConfiguration](valuecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [sidebarCellConfiguration](sidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in a sidebar list. _(deprecated)_
- [sidebarSubtitleCellConfiguration](sidebarsubtitlecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text. _(deprecated)_
- [accompaniedSidebarCellConfiguration](accompaniedsidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in an accompanied sidebar list.

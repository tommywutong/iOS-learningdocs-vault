---
title: groupedHeaderConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/groupedheaderconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/groupedheaderconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/groupedheaderconfiguration.json'
content_hash: 'sha256:e079ae8e96f90481'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# groupedHeaderConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a header in a grouped list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) groupedHeaderConfiguration;
```

## Return Value

The default configuration for a header in a grouped list.

## Discussion

Create this configuration to update the content and styling of a header in a table view or collection view list.

For an appearance consistent with system defaults, display your header in a table view or collection view list that you configure with one of the following enumeration cases:

- [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md)
- [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md)
- [UICollectionLayoutListAppearanceGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md)
- [UICollectionLayoutListAppearanceInsetGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md)

Configure the background of your header using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md) options below. Match the background of your header to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listGroupedHeaderFooterConfiguration](../uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration.md) | [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md), [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md), [UICollectionLayoutListAppearanceGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md), [UICollectionLayoutListAppearanceInsetGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md) |

## See Also

### Creating header and footer configurations

- [plainHeaderConfiguration](plainheaderconfiguration.md) — Creates the default configuration you use to style a header in a plain list. _(deprecated)_
- [plainFooterConfiguration](plainfooterconfiguration.md) — Creates the default configuration you use to style a footer in a plain list. _(deprecated)_
- [groupedFooterConfiguration](groupedfooterconfiguration.md) — Creates the default configuration you use to style a footer in a grouped list. _(deprecated)_
- [prominentInsetGroupedHeaderConfiguration](prominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [extraProminentInsetGroupedHeaderConfiguration](extraprominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [sidebarHeaderConfiguration](sidebarheaderconfiguration.md) — Creates the default configuration you use to style a header in a sidebar list. _(deprecated)_

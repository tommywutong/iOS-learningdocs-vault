---
title: plainFooterConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/plainfooterconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/plainfooterconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/plainfooterconfiguration.json'
content_hash: 'sha256:180c108805adc28d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# plainFooterConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a footer in a plain list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) plainFooterConfiguration;
```

## Return Value

The default configuration for a footer in a plain list.

## Discussion

Create this configuration to update the content and styling of a footer in a table view or collection view list.

For an appearance consistent with system defaults, display your footer in a table view or collection view list that you configure with one of the following enumeration cases:

- [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md)
- [UICollectionLayoutListAppearancePlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md)
- [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md)

Configure the background of your footer using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md) options below. Match the background of your footer to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listPlainHeaderFooterConfiguration](../uibackgroundconfiguration-c.class/listplainheaderfooterconfiguration.md) | [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md), [UICollectionLayoutListAppearancePlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md), [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) |

## See Also

### Creating header and footer configurations

- [plainHeaderConfiguration](plainheaderconfiguration.md) — Creates the default configuration you use to style a header in a plain list. _(deprecated)_
- [groupedHeaderConfiguration](groupedheaderconfiguration.md) — Creates the default configuration you use to style a header in a grouped list. _(deprecated)_
- [groupedFooterConfiguration](groupedfooterconfiguration.md) — Creates the default configuration you use to style a footer in a grouped list. _(deprecated)_
- [prominentInsetGroupedHeaderConfiguration](prominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [extraProminentInsetGroupedHeaderConfiguration](extraprominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [sidebarHeaderConfiguration](sidebarheaderconfiguration.md) — Creates the default configuration you use to style a header in a sidebar list. _(deprecated)_

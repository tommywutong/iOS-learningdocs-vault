---
title: extraProminentInsetGroupedHeaderConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/extraprominentinsetgroupedheaderconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/extraprominentinsetgroupedheaderconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/extraprominentinsetgroupedheaderconfiguration.json'
content_hash: 'sha256:26c2d1faf0b97b04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# extraProminentInsetGroupedHeaderConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style an extra prominent header in an inset grouped list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) extraProminentInsetGroupedHeaderConfiguration;
```

## Return Value

The default configuration for an extra prominent header in an inset grouped list.

## Discussion

Create this configuration to update the content and styling of a header in a table view or collection view list.

For an appearance consistent with system defaults, display your header in a table view or collection view list that you configure with one of the following enumeration cases:

- [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md)
- [UICollectionLayoutListAppearanceInsetGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md)

Configure the background of your header using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md) options below. Match the background of your header to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listGroupedHeaderFooterConfiguration](../uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration.md) | [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md), [UICollectionLayoutListAppearanceInsetGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md) |

## See Also

### Creating header and footer configurations

- [plainHeaderConfiguration](plainheaderconfiguration.md) — Creates the default configuration you use to style a header in a plain list. _(deprecated)_
- [plainFooterConfiguration](plainfooterconfiguration.md) — Creates the default configuration you use to style a footer in a plain list. _(deprecated)_
- [groupedHeaderConfiguration](groupedheaderconfiguration.md) — Creates the default configuration you use to style a header in a grouped list. _(deprecated)_
- [groupedFooterConfiguration](groupedfooterconfiguration.md) — Creates the default configuration you use to style a footer in a grouped list. _(deprecated)_
- [prominentInsetGroupedHeaderConfiguration](prominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [sidebarHeaderConfiguration](sidebarheaderconfiguration.md) — Creates the default configuration you use to style a header in a sidebar list. _(deprecated)_

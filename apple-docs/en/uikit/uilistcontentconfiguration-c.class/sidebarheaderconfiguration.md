---
title: sidebarHeaderConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/sidebarheaderconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/sidebarheaderconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/sidebarheaderconfiguration.json'
content_hash: 'sha256:1bac6d3f01e78732'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# sidebarHeaderConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a header in a sidebar list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) sidebarHeaderConfiguration;
```

## Return Value

The default configuration for a header in a sidebar list.

## Discussion

Create this configuration to update the content and styling of a header in a sidebar collection view list.

For an appearance consistent with system defaults, display your header in a sidebar collection view list that you configure with the [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) enumeration case.

Configure the background of your cell using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listSidebarHeaderConfiguration](../uibackgroundconfiguration-c.class/listsidebarheaderconfiguration.md) | [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) |

## See Also

### Creating header and footer configurations

- [plainHeaderConfiguration](plainheaderconfiguration.md) — Creates the default configuration you use to style a header in a plain list. _(deprecated)_
- [plainFooterConfiguration](plainfooterconfiguration.md) — Creates the default configuration you use to style a footer in a plain list. _(deprecated)_
- [groupedHeaderConfiguration](groupedheaderconfiguration.md) — Creates the default configuration you use to style a header in a grouped list. _(deprecated)_
- [groupedFooterConfiguration](groupedfooterconfiguration.md) — Creates the default configuration you use to style a footer in a grouped list. _(deprecated)_
- [prominentInsetGroupedHeaderConfiguration](prominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [extraProminentInsetGroupedHeaderConfiguration](extraprominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.

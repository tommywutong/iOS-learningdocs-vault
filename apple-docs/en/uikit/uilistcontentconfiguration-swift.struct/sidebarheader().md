---
title: sidebarHeader()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/sidebarheader()
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/sidebarheader()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/sidebarheader%28%29.json'
content_hash: 'sha256:e5d639856e33bda5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# sidebarHeader()

<sub>Type Method</sub>

Creates the default configuration you use to style a header in a sidebar list.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func sidebarHeader() -> UIListContentConfiguration
```

## Return Value

The default configuration for a header in a sidebar list.

## Discussion

Create this configuration to update the content and styling of a header in a sidebar collection view list.

For an appearance consistent with system defaults, display your header in a sidebar collection view list that you configure with the [UICollectionLayoutListConfiguration.Appearance.sidebar](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) enumeration case.

Configure the background of your cell using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listSidebarHeader()](<../uibackgroundconfiguration-swift.struct/listsidebarheader().md>) | [UICollectionLayoutListConfiguration.Appearance.sidebar](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) |

## See Also

### Creating header and footer configurations

- [plainHeader()](<plainheader().md>) — Creates the default configuration you use to style a header in a plain list.
- [plainFooter()](<plainfooter().md>) — Creates the default configuration you use to style a footer in a plain list.
- [groupedHeader()](<groupedheader().md>) — Creates the default configuration you use to style a header in a grouped list.
- [groupedFooter()](<groupedfooter().md>) — Creates the default configuration you use to style a footer in a grouped list.
- [prominentInsetGroupedHeader()](<prominentinsetgroupedheader().md>) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [extraProminentInsetGroupedHeader()](<extraprominentinsetgroupedheader().md>) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.

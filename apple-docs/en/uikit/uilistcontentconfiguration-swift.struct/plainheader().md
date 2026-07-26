---
title: plainHeader()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/plainheader()
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/plainheader()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/plainheader%28%29.json'
content_hash: 'sha256:7effc01d05b84f03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# plainHeader()

<sub>Type Method</sub>

Creates the default configuration you use to style a header in a plain list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func plainHeader() -> UIListContentConfiguration
```

## Return Value

The default configuration for a header in a plain list.

## Discussion

Create this configuration to update the content and styling of a header in a table view or collection view list.

For an appearance consistent with system defaults, display your header in a table view or collection view list that you configure with one of the following enumeration cases:

- [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md)
- [UICollectionLayoutListConfiguration.Appearance.plain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md)
- [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md)

Configure the background of your header using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md) options below. Match the background of your header to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listPlainHeaderFooter()](<../uibackgroundconfiguration-swift.struct/listplainheaderfooter().md>) | [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md), [UICollectionLayoutListConfiguration.Appearance.plain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md), [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) |

## See Also

### Creating header and footer configurations

- [plainFooter()](<plainfooter().md>) — Creates the default configuration you use to style a footer in a plain list.
- [groupedHeader()](<groupedheader().md>) — Creates the default configuration you use to style a header in a grouped list.
- [groupedFooter()](<groupedfooter().md>) — Creates the default configuration you use to style a footer in a grouped list.
- [prominentInsetGroupedHeader()](<prominentinsetgroupedheader().md>) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [extraProminentInsetGroupedHeader()](<extraprominentinsetgroupedheader().md>) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [sidebarHeader()](<sidebarheader().md>) — Creates the default configuration you use to style a header in a sidebar list.

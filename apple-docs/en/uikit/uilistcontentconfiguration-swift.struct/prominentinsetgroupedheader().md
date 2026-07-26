---
title: prominentInsetGroupedHeader()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/prominentinsetgroupedheader()
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/prominentinsetgroupedheader()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/prominentinsetgroupedheader%28%29.json'
content_hash: 'sha256:eecc515dfc531d37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# prominentInsetGroupedHeader()

<sub>Type Method</sub>

Creates the default configuration you use to style a prominent header in an inset grouped list.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func prominentInsetGroupedHeader() -> UIListContentConfiguration
```

## Return Value

The default configuration for a prominent header in an inset grouped list.

## Discussion

Create this configuration to update the content and styling of a header in a table view or collection view list.

For an appearance consistent with system defaults, display your header in a table view or collection view list that you configure with one of the following enumeration cases:

- [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md)
- [UICollectionLayoutListConfiguration.Appearance.insetGrouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md)

Configure the background of your header using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md) options below. Match the background of your header to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listGroupedHeaderFooter()](<../uibackgroundconfiguration-swift.struct/listgroupedheaderfooter().md>) | [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md), [UICollectionLayoutListConfiguration.Appearance.insetGrouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md) |

## See Also

### Creating header and footer configurations

- [plainHeader()](<plainheader().md>) — Creates the default configuration you use to style a header in a plain list.
- [plainFooter()](<plainfooter().md>) — Creates the default configuration you use to style a footer in a plain list.
- [groupedHeader()](<groupedheader().md>) — Creates the default configuration you use to style a header in a grouped list.
- [groupedFooter()](<groupedfooter().md>) — Creates the default configuration you use to style a footer in a grouped list.
- [extraProminentInsetGroupedHeader()](<extraprominentinsetgroupedheader().md>) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [sidebarHeader()](<sidebarheader().md>) — Creates the default configuration you use to style a header in a sidebar list.

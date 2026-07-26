---
title: listGroupedHeaderFooterConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration.json'
content_hash: 'sha256:7ce69e33ece6b534'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md)

# listGroupedHeaderFooterConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a grouped list header or footer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) listGroupedHeaderFooterConfiguration;
```

## Return Value

The default configuration for a grouped list header or footer.

## Discussion

> [!warning] Deprecated
> Use [listHeader()](<../uibackgroundconfiguration-swift.struct/listheader().md>) or [listFooter()](<../uibackgroundconfiguration-swift.struct/listfooter().md>) instead.

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a grouped list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in these contexts:

- A table view that you configure with the [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md) or [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md) enumeration cases.
- A a collection view list that you configure with the [UICollectionLayoutListAppearanceGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md) or [UICollectionLayoutListAppearanceInsetGrouped](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md) enumeration cases.

## See Also

### Creating header and footer background configurations

- [listPlainHeaderFooterConfiguration](listplainheaderfooterconfiguration.md) — Creates the default configuration you use to style a plain list header or footer. _(deprecated)_
- [listSidebarHeaderConfiguration](listsidebarheaderconfiguration.md) — Creates the default configuration you use to style a sidebar list header. _(deprecated)_

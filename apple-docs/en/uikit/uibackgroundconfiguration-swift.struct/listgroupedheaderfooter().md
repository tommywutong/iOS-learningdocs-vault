---
title: listGroupedHeaderFooter()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-swift.struct/listgroupedheaderfooter()
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listgroupedheaderfooter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-swift.struct/listgroupedheaderfooter%28%29.json'
content_hash: 'sha256:fb67250ce34b983b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md)

# listGroupedHeaderFooter()

<sub>Type Method</sub>

Creates the default configuration you use to style a grouped list header or footer.

> [!warning] Deprecated
> Use [listHeader()](<listheader().md>) or [listFooter()](<listfooter().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func listGroupedHeaderFooter() -> UIBackgroundConfiguration
```

## Return Value

The default configuration for a grouped list header or footer.

## Discussion

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a grouped list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in these contexts:

- A table view that you configure with the [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md) or [UITableViewStyleInsetGrouped](../uitableview/style-swift.enum/insetgrouped.md) enumeration cases.
- A a collection view list that you configure with the [UICollectionLayoutListConfiguration.Appearance.grouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md) or [UICollectionLayoutListConfiguration.Appearance.insetGrouped](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md) enumeration cases.

## See Also

### Creating header and footer background configurations

- [listPlainHeaderFooter()](<listplainheaderfooter().md>) — Creates the default configuration you use to style a plain list header or footer. _(deprecated)_
- [listSidebarHeader()](<listsidebarheader().md>) — Creates the default configuration you use to style a sidebar list header. _(deprecated)_

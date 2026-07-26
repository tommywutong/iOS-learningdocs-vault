---
title: listPlainHeaderFooter()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-swift.struct/listplainheaderfooter()
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listplainheaderfooter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-swift.struct/listplainheaderfooter%28%29.json'
content_hash: 'sha256:a1b9e62abfee270f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md)

# listPlainHeaderFooter()

<sub>Type Method</sub>

Creates the default configuration you use to style a plain list header or footer.

> [!warning] Deprecated
> Use [listHeader()](<listheader().md>) or [listFooter()](<listfooter().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func listPlainHeaderFooter() -> UIBackgroundConfiguration
```

## Return Value

The default configuration for a plain list header or footer.

## Discussion

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a plain list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in these contexts:

- A table view that you configure with the [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md) enumeration case.
- A collection view list that you configure with the [UICollectionLayoutListConfiguration.Appearance.plain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) or [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) enumeration cases.

## See Also

### Creating header and footer background configurations

- [listGroupedHeaderFooter()](<listgroupedheaderfooter().md>) — Creates the default configuration you use to style a grouped list header or footer. _(deprecated)_
- [listSidebarHeader()](<listsidebarheader().md>) — Creates the default configuration you use to style a sidebar list header. _(deprecated)_

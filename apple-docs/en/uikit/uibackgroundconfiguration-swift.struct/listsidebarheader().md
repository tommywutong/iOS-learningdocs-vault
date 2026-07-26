---
title: listSidebarHeader()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-swift.struct/listsidebarheader()
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listsidebarheader()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-swift.struct/listsidebarheader%28%29.json'
content_hash: 'sha256:59c2f4162206d190'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md)

# listSidebarHeader()

<sub>Type Method</sub>

Creates the default configuration you use to style a sidebar list header.

> [!warning] Deprecated
> Use [listHeader()](<listheader().md>) or [listFooter()](<listfooter().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func listSidebarHeader() -> UIBackgroundConfiguration
```

## Return Value

The default configuration for a sidebar list header.

## Discussion

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a sidebar list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in a collection view list that you configure with the [UICollectionLayoutListConfiguration.Appearance.sidebar](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) enumeration case.

## See Also

### Creating header and footer background configurations

- [listPlainHeaderFooter()](<listplainheaderfooter().md>) — Creates the default configuration you use to style a plain list header or footer. _(deprecated)_
- [listGroupedHeaderFooter()](<listgroupedheaderfooter().md>) — Creates the default configuration you use to style a grouped list header or footer. _(deprecated)_

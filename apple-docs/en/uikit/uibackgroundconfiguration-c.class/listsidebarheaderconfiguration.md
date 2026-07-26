---
title: listSidebarHeaderConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-c.class/listsidebarheaderconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listsidebarheaderconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-c.class/listsidebarheaderconfiguration.json'
content_hash: 'sha256:58036c59db865289'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md)

# listSidebarHeaderConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a sidebar list header.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) listSidebarHeaderConfiguration;
```

## Return Value

The default configuration for a sidebar list header.

## Discussion

> [!warning] Deprecated
> Use [listHeader()](<../uibackgroundconfiguration-swift.struct/listheader().md>) or [listFooter()](<../uibackgroundconfiguration-swift.struct/listfooter().md>) instead.

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a sidebar list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in a collection view list that you configure with the [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) enumeration case.

## See Also

### Creating header and footer background configurations

- [listPlainHeaderFooterConfiguration](listplainheaderfooterconfiguration.md) — Creates the default configuration you use to style a plain list header or footer. _(deprecated)_
- [listGroupedHeaderFooterConfiguration](listgroupedheaderfooterconfiguration.md) — Creates the default configuration you use to style a grouped list header or footer. _(deprecated)_

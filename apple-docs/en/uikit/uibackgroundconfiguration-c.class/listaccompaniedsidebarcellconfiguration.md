---
title: listAccompaniedSidebarCellConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundconfiguration-c.class/listaccompaniedsidebarcellconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listaccompaniedsidebarcellconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-c.class/listaccompaniedsidebarcellconfiguration.json'
content_hash: 'sha256:cce402b53b4badf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md)

# listAccompaniedSidebarCellConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a cell in an accompanied sidebar list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) listAccompaniedSidebarCellConfiguration;
```

## Return Value

The default configuration for a cell in an accompanied sidebar list.

## Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a cell in an accompanied sidebar collection view list, including highlighted and selected states. An accompanied sidebar collection view list is a list that’s in the primary column of a split view controller, accompanied by another list in the split view controller’s supplementary column.

For an appearance consistent with system defaults, use this background configuration for a cell in an accompanied sidebar collection view list that you configure with the [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) or [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) enumeration case.

## See Also

### Creating cell background configurations

- [listPlainCellConfiguration](listplaincellconfiguration.md) — Creates the default configuration you use to style a cell in a plain list. _(deprecated)_
- [listGroupedCellConfiguration](listgroupedcellconfiguration.md) — Creates the default configuration you use to style a cell in a grouped list. _(deprecated)_
- [listSidebarCellConfiguration](listsidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in a sidebar list. _(deprecated)_

---
title: listSidebarCellConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibackgroundconfiguration-c.class/listsidebarcellconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listsidebarcellconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-c.class/listsidebarcellconfiguration.json'
content_hash: 'sha256:d1fe73fafc2f3464'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md)

# listSidebarCellConfiguration

<sub>Type Method</sub>

Creates the default configuration you use to style a cell in a sidebar list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) listSidebarCellConfiguration;
```

## Return Value

The default configuration for a cell in a sidebar list.

## Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a cell in a sidebar collection view list, including highlighted and selected states.

For an appearance consistent with system defaults, use this background configuration for a cell in a collection view list that you configure with the [UICollectionLayoutListAppearanceSidebar](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) or [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) enumeration case.

## See Also

### Creating cell background configurations

- [listPlainCellConfiguration](listplaincellconfiguration.md) — Creates the default configuration you use to style a cell in a plain list. _(deprecated)_
- [listGroupedCellConfiguration](listgroupedcellconfiguration.md) — Creates the default configuration you use to style a cell in a grouped list. _(deprecated)_
- [listAccompaniedSidebarCellConfiguration](listaccompaniedsidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in an accompanied sidebar list.

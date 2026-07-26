---
title: accompaniedSidebarCell()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/accompaniedsidebarcell()
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/accompaniedsidebarcell()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/accompaniedsidebarcell%28%29.json'
content_hash: 'sha256:a67d7deaabb50501'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# accompaniedSidebarCell()

<sub>Type Method</sub>

Creates the default configuration you use to style a cell in an accompanied sidebar list.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func accompaniedSidebarCell() -> UIListContentConfiguration
```

## Return Value

The default configuration for a cell in an accompanied sidebar list.

## Discussion

Create this configuration to update the content and styling of a cell in an accompanied sidebar collection view list, where the list is in the primary column of a split view controller, accompanied by another list in the split view controller’s supplementary column. When you apply this configuration to a cell, the cell displays one label, which resizes automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in an accompanied sidebar collection view list that you configure with one of the following enumeration cases:

- [UICollectionLayoutListConfiguration.Appearance.sidebar](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md)
- [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md)

Configure the background of your cell using one of the [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
|---|---|
| [listAccompaniedSidebarCell()](<../uibackgroundconfiguration-swift.struct/listaccompaniedsidebarcell().md>) | [UICollectionLayoutListConfiguration.Appearance.sidebar](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md), [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) |

## See Also

### Creating default cell configurations

- [cell()](<cell().md>) — Creates the default configuration you use to style a cell in a list.
- [subtitleCell()](<subtitlecell().md>) — Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [valueCell()](<valuecell().md>) — Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [sidebarCell()](<sidebarcell().md>) — Creates the default configuration you use to style a cell in a sidebar list.
- [sidebarSubtitleCell()](<sidebarsubtitlecell().md>) — Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.
- [accompaniedSidebarSubtitleCell()](<accompaniedsidebarsubtitlecell().md>) — Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.

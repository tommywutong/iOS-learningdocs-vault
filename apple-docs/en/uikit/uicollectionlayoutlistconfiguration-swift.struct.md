---
title: UICollectionLayoutListConfiguration
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct.json'
content_hash: 'sha256:419873e654b6b512'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionLayoutListConfiguration

<sub>Structure</sub>

A configuration for creating a list layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UICollectionLayoutListConfiguration
```

## Overview

Use this configuration to create a list section for a compositional layout ([UICollectionViewCompositionalLayout](uicollectionviewcompositionallayout.md)), or a layout containing only list sections. The following example shows how to create a compositional layout that contains only list sections by applying the same configuration to each section in the list layout:

```swift
let configuration = UICollectionLayoutListConfiguration(appearance: .sidebar)
let layout = UICollectionViewCompositionalLayout.list(using: configuration)
```

To implement different list configurations for different sections, use a compositional layout’s section provider to create each section with its own list configuration.

```swift
let layout = UICollectionViewCompositionalLayout() { sectionIndex, layoutEnvironment in
    
    var configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
    configuration.headerMode = sectionIndex == 0 ? .supplementary : .none
    
    let section = NSCollectionLayoutSection.list(using: configuration,
                                                 layoutEnvironment: layoutEnvironment)
    
    return section
}
```

## Topics

### Creating a list layout configuration

- [init(appearance:)](<uicollectionlayoutlistconfiguration-swift.struct/init(appearance_).md>) — Creates a list layout configuration with the specified appearance.

### Configuring appearance

- [appearance](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.property.md) — The overall appearance of the list.
- [backgroundColor](uicollectionlayoutlistconfiguration-swift.struct/backgroundcolor.md) — The background color of the list.
- [Appearance](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum.md) — Constants that describe the appearance of the list.

### Configuring separators

- [showsSeparators](uicollectionlayoutlistconfiguration-swift.struct/showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration.md) — The section’s preferred configuration for list separators.
- [UIListSeparatorConfiguration](uilistseparatorconfiguration-swift.struct.md) — A configuration that controls the list separator appearance in a list section.
- [itemSeparatorHandler](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property.md) — The closure that provides granular control over the list separator appearance of each item.
- [ItemSeparatorHandler](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.typealias.md) — A closure that provides granular control over list separator appearance.

### Configuring headers and footers

- [headerMode](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.property.md) — The type of header to use for the list.
- [footerMode](uicollectionlayoutlistconfiguration-swift.struct/footermode-swift.property.md) — The type of footer to use for the list.
- [HeaderMode](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum.md) — Constants that describe the list’s header mode.
- [FooterMode](uicollectionlayoutlistconfiguration-swift.struct/footermode-swift.enum.md) — Constants that describe the list’s footer mode.
- [headerTopPadding](uicollectionlayoutlistconfiguration-swift.struct/headertoppadding.md) — The amount of padding above each section header.

### Customizing swipe actions

- [leadingSwipeActionsConfigurationProvider](uicollectionlayoutlistconfiguration-swift.struct/leadingswipeactionsconfigurationprovider.md) — The closure that provides the set of actions to display when swiping on the leading edge of the cell.
- [trailingSwipeActionsConfigurationProvider](uicollectionlayoutlistconfiguration-swift.struct/trailingswipeactionsconfigurationprovider.md) — The closure that provides the set of actions to display when swiping on the trailing edge of the cell.
- [SwipeActionsConfigurationProvider](uicollectionlayoutlistconfiguration-swift.struct/swipeactionsconfigurationprovider.md) — A closure that configures the swipe actions for a cell.

### Managing content-hugging behavior

- [contentHuggingElements](uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.property.md) — A setting that determines which type of items tightly hug their content.
- [ContentHuggingElements](uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.struct.md) — Constants that determine which types of items in a collection view tightly hug their content.

## See Also

### Related Documentation

- [list(using:layoutEnvironment:)](<nscollectionlayoutsection/list(using_layoutenvironment_).md>) — Creates a list section with the specified list configuration and layout environment.

### Creating a list layout

- [list(using:)](<uicollectionviewcompositionallayout/list(using_).md>) — Creates a compositional layout that contains only list sections of the specified configuration.

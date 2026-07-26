---
title: UIListSeparatorConfiguration
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistseparatorconfiguration-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uilistseparatorconfiguration-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistseparatorconfiguration-swift.struct.json'
content_hash: 'sha256:e6a9bfdbbcd082da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIListSeparatorConfiguration

<sub>Structure</sub>

A configuration that controls the list separator appearance in a list section.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIListSeparatorConfiguration
```

## Overview

To specify list separator appearance for a section, set a default sectionwide [separatorConfiguration](uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration.md) on your [UICollectionLayoutListConfiguration](uicollectionlayoutlistconfiguration-swift.struct.md) when you create your list.

```swift
var listConfig = UICollectionLayoutListConfiguration(appearance: .plain)
listConfig.separatorConfiguration.color = .tertiarySystemFill
let layout = UICollectionViewCompositionalLayout.list(using: listConfig)
```

To override list separator appearance on a per-item basis, use the [itemSeparatorHandler](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property.md) property.

```swift
var listConfig = UICollectionLayoutListConfiguration(appearance: .plain)
listConfig.separatorConfiguration.color = .tertiarySystemFill

let indexPathToHide = IndexPath()
 
listConfig.itemSeparatorHandler = { (indexPath, sectionSeparatorConfiguration) in    
    var configuration = sectionSeparatorConfiguration
    if indexPath == indexPathToHide {
        configuration.bottomSeparatorVisibility = .hidden    
    }    
    return configuration
}

let layout = UICollectionViewCompositionalLayout.list(using: listConfig)
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a list separator configuration

- [init(listAppearance:)](<uilistseparatorconfiguration-swift.struct/init(listappearance_).md>) — Creates a list separator configuration with default values according to the specified list appearance.

### Controlling separator visibility

- [topSeparatorVisibility](uilistseparatorconfiguration-swift.struct/topseparatorvisibility.md) — The visibility of the top separator for the item the configuration applies to.
- [bottomSeparatorVisibility](uilistseparatorconfiguration-swift.struct/bottomseparatorvisibility.md) — The visibility of the bottom separator for the item the configuration applies to.
- [Visibility](uilistseparatorconfiguration-swift.struct/visibility.md) — Constants that define the visibility of list separators.

### Configuring separator insets

- [topSeparatorInsets](uilistseparatorconfiguration-swift.struct/topseparatorinsets.md) — Insets to apply to the top separator of the item the configuration applies to.
- [bottomSeparatorInsets](uilistseparatorconfiguration-swift.struct/bottomseparatorinsets.md) — Insets to apply to the bottom separator of the item the configuration applies to.
- [automaticInsets](uilistseparatorconfiguration-swift.struct/automaticinsets.md) — A constant that specifies a placeholder size for separator insets.

### Configuring separator appearance

- [color](uilistseparatorconfiguration-swift.struct/color.md) — The color to use for the separators of the item the configuration applies to.
- [multipleSelectionColor](uilistseparatorconfiguration-swift.struct/multipleselectioncolor.md) — The color to use for the separators of the item the configuration applies to when the item is in a multiple-selection group.
- [visualEffect](uilistseparatorconfiguration-swift.struct/visualeffect.md) — The visual effect to use for the separators of the item the configuration applies to.

## See Also

### Configuring separators

- [showsSeparators](uicollectionlayoutlistconfiguration-swift.struct/showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration.md) — The section’s preferred configuration for list separators.
- [itemSeparatorHandler](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property.md) — The closure that provides granular control over the list separator appearance of each item.
- [ItemSeparatorHandler](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.typealias.md) — A closure that provides granular control over list separator appearance.

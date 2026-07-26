---
title: UICellConfigurationState
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellconfigurationstate-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellconfigurationstate-swift.struct.json'
content_hash: 'sha256:dc8f81bb5a74224f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellConfigurationState

<sub>Structure</sub>

A structure that encapsulates a cell’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UICellConfigurationState
```

## Overview

A cell configuration state encompasses a trait collection along with all of the common states that affect a cell’s appearance — view states like selected, focused, or disabled, and cell states like editing or swiped. A cell configuration state encapsulates the inputs that configure a cell for any possible state or combination of states. You use a cell configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) method in your cell subclass and use the state parameter. Outside of this method, you can get a cell’s configuration state by using its [configurationState](uicollectionviewcell/configurationstate-4u37h.md) property.

You can create your own custom states to add to a cell configuration state by defining a custom state key using [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [UIConfigurationState](uiconfigurationstate-8d7pd.md)

## Topics

### Managing view configuration states

- [isSelected](uicellconfigurationstate-swift.struct/isselected.md) — A Boolean value that indicates whether the cell is in a selected state.
- [isHighlighted](uicellconfigurationstate-swift.struct/ishighlighted.md) — A Boolean value that indicates whether the cell is in a highlighted state.
- [isFocused](uicellconfigurationstate-swift.struct/isfocused.md) — A Boolean value that indicates whether the cell is in a focused state.
- [isDisabled](uicellconfigurationstate-swift.struct/isdisabled.md) — A Boolean value that indicates whether the cell is in a disabled state.
- [isPinned](uicellconfigurationstate-swift.struct/ispinned.md) — A Boolean value that indicates whether the view is in a pinned state.

### Managing cell configuration states

- [isEditing](uicellconfigurationstate-swift.struct/isediting.md) — A Boolean value that indicates whether the cell is in editing mode.
- [isSwiped](uicellconfigurationstate-swift.struct/isswiped.md) — A Boolean value that indicates whether the cell is in a swiped state.
- [isExpanded](uicellconfigurationstate-swift.struct/isexpanded.md) — A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [isReordering](uicellconfigurationstate-swift.struct/isreordering.md) — A Boolean value that indicates whether the cell is reordering.
- [cellDragState](uicellconfigurationstate-swift.struct/celldragstate.md) — The cell’s drag state.
- [cellDropState](uicellconfigurationstate-swift.struct/celldropstate.md) — The cell’s drop state.
- [DragState](uicellconfigurationstate-swift.struct/dragstate.md) — Constants that describe the cell’s drag state.
- [DropState](uicellconfigurationstate-swift.struct/dropstate.md) — Constants that describe the cell’s drop state.

## See Also

### Configuration states

- [UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md) — A structure that encapsulates a view’s state.
- [UIConfigurationState](uiconfigurationstate-8d7pd.md) — The requirements for an object that encapsulates a view’s state.
- [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md) — A key that defines a custom state for a view.

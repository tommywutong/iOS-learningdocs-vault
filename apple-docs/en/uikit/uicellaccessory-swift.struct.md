---
title: UICellAccessory
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct.json'
content_hash: 'sha256:dce9de0636b85770'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellAccessory

<sub>Structure</sub>

An accessory in a collection view list cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UICellAccessory
```

## Overview

A cell accessory is a visual element that you can add to a list cell ([UICollectionViewListCell](uicollectionviewlistcell.md)). You use a cell accessory as a visual indicator or to let a user perform a cell-specific action like selecting, reordering, or deleting the cell. A cell accessory appears either on the leading or the trailing edge of a cell, outside of the cell’s content view.

UIKit defines a set of standard system cell accessories. System accessories have default system-defined appearances, but you can make some customizations to them, like setting a custom tint color. You can’t customize the placement of system accessories. If you want additional customization, you can create a custom accessory with [customView(configuration:)](<uicellaccessory-swift.struct/customview(configuration_).md>).

You add accessories to a list cell by setting its [accessories](uicollectionviewlistcell/accessories-88j0f.md) array.

```swift
cell.accessories = [ 
    .checkmark(), 
    .disclosureIndicator(options: .init(tintColor: .systemGray)), 
    .delete(),
    .reorder() 
]
```

> [!important] Important
> The system throws an exception if you include more than one instance of any system accessory. You can include multiple custom accessories.

## Topics

### Creating a disclosure indicator

- [disclosureIndicator(displayed:options:)](<uicellaccessory-swift.struct/disclosureindicator(displayed_options_).md>) — Creates a disclosure indicator system accessory with the specified display state and configuration options.
- [DisclosureIndicatorOptions](uicellaccessory-swift.struct/disclosureindicatoroptions.md) — Configuration options for a disclosure indicator.

### Creating an outline disclosure

- [outlineDisclosure(displayed:options:actionHandler:)](<uicellaccessory-swift.struct/outlinedisclosure(displayed_options_actionhandler_).md>) — Creates an outline disclosure system accessory with the specified display state, configuration options, and optional action handler.
- [OutlineDisclosureOptions](uicellaccessory-swift.struct/outlinedisclosureoptions.md) — Configuration options for an outline disclosure.

### Creating a popup menu accessory

- [popUpMenu(_:displayed:options:selectedElementDidChangeHandler:)](<uicellaccessory-swift.struct/popupmenu(__displayed_options_selectedelementdidchangehandler_).md>) — Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.
- [MenuSelectedElementDidChangeHandler](uicellaccessory-swift.struct/menuselectedelementdidchangehandler.md) — A closure type that defines a handler to perform when a user selects an element in the menu.
- [PopUpMenuOptions](uicellaccessory-swift.struct/popupmenuoptions.md) — Configuration options for a popup menu accessory.

### Creating a checkmark accessory

- [checkmark(displayed:options:)](<uicellaccessory-swift.struct/checkmark(displayed_options_).md>) — Creates a checkmark system accessory with the specified display state and configuration options.
- [CheckmarkOptions](uicellaccessory-swift.struct/checkmarkoptions.md) — Configuration options for a checkmark accessory.

### Creating a delete accessory

- [delete(displayed:options:actionHandler:)](<uicellaccessory-swift.struct/delete(displayed_options_actionhandler_).md>) — Creates a delete system accessory with the specified display state, configuration options, and optional action handler.
- [DeleteOptions](uicellaccessory-swift.struct/deleteoptions.md) — Configuration options for a delete accessory.

### Creating an insert accessory

- [insert(displayed:options:actionHandler:)](<uicellaccessory-swift.struct/insert(displayed_options_actionhandler_).md>) — Creates an insert system accessory with the specified display state, configuration options, and optional action handler.
- [InsertOptions](uicellaccessory-swift.struct/insertoptions.md) — Configuration options for an insert accessory.

### Creating a reorder accessory

- [reorder(displayed:options:)](<uicellaccessory-swift.struct/reorder(displayed_options_).md>) — Creates a reorder system accessory with the specified display state and configuration options.
- [ReorderOptions](uicellaccessory-swift.struct/reorderoptions.md) — Configuration options for a reorder accessory.

### Creating a multiselect accessory

- [multiselect(displayed:options:)](<uicellaccessory-swift.struct/multiselect(displayed_options_).md>) — Creates a multiselect system accessory with the specified display state and configuration options.
- [MultiselectOptions](uicellaccessory-swift.struct/multiselectoptions.md) — Configuration options for a multiselect accessory.

### Creating a label accessory

- [label(text:displayed:options:)](<uicellaccessory-swift.struct/label(text_displayed_options_).md>) — Creates a label system accessory with the specified text, display state, and configuration options.
- [LabelOptions](uicellaccessory-swift.struct/labeloptions.md) — Configuration options for a label accessory.

### Creating a detail accessory

- [detail(displayed:options:actionHandler:)](<uicellaccessory-swift.struct/detail(displayed_options_actionhandler_).md>) — Creates a detail system accessory with the specified display state, configuration options, and optional action handler.
- [DetailOptions](uicellaccessory-swift.struct/detailoptions.md) — Configuration options for a detail accessory.

### Creating a custom accessory

- [customView(configuration:)](<uicellaccessory-swift.struct/customview(configuration_).md>) — Creates a custom view accessory.
- [CustomViewConfiguration](uicellaccessory-swift.struct/customviewconfiguration.md) — Configuration options for a custom accessory.

### Checking the accessory’s type

- [accessoryType](uicellaccessory-swift.struct/accessorytype-swift.property.md) — The type of the cell accessory.
- [AccessoryType](uicellaccessory-swift.struct/accessorytype-swift.enum.md) — Constants that describe the type of the cell accessory.

### Customizing appearance and placement

- [LayoutDimension](uicellaccessory-swift.struct/layoutdimension.md) — Constants that describe the layout dimension for the accessory.
- [Placement](uicellaccessory-swift.struct/placement.md) — Constants that describe the placement of the accessory within the cell.
- [DisplayedState](uicellaccessory-swift.struct/displayedstate.md) — Constants that describe the cell-editing states that the accessory appears in.

### Performing accessory actions

- [ActionHandler](uicellaccessory-swift.struct/actionhandler.md) — A closure that the system calls when a user taps a cell accessory.

## See Also

### Managing cell accessories

- [accessories](uicollectionviewlistcell/accessories-8nui4.md) — An array of the accessories that decorate the cell.

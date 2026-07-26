---
title: 'popUpMenu(_:displayed:options:selectedElementDidChangeHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/popupmenu(_:displayed:options:selectedelementdidchangehandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/popupmenu(_:displayed:options:selectedelementdidchangehandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/popupmenu%28_%3Adisplayed%3Aoptions%3Aselectedelementdidchangehandler%3A%29.json'
content_hash: 'sha256:7321fd9d1f70b622'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# popUpMenu(_:displayed:options:selectedElementDidChangeHandler:)

<sub>Type Method</sub>

Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func popUpMenu(_ menu: UIMenu, displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.PopUpMenuOptions = PopUpMenuOptions(), selectedElementDidChangeHandler: UICellAccessory.MenuSelectedElementDidChangeHandler? = nil) -> UICellAccessory
```

## Parameters

- `menu` — The menu to display when a user taps the popup menu accessory.

- `displayed` — The cell-editing states that the popup menu accessory appears in. This parameter has a default value of [UICellAccessory.DisplayedState.always](displayedstate/always.md).

- `options` — Configuration options for the popup menu accessory. See [PopUpMenuOptions](popupmenuoptions.md) for possible configuration options.

- `selectedElementDidChangeHandler` — An optional closure that the system calls when a user selects an element in the menu.

## Return Value

A configured popup menu cell accessory that appears as a pair of chevrons that point upward and downward. This accessory indicates that tapping anywhere in the cell presents a popup menu. This accessory appears on the trailing edge of the cell.

## See Also

### Creating a popup menu accessory

- [MenuSelectedElementDidChangeHandler](menuselectedelementdidchangehandler.md) — A closure type that defines a handler to perform when a user selects an element in the menu.
- [PopUpMenuOptions](popupmenuoptions.md) — Configuration options for a popup menu accessory.

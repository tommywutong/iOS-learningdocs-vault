---
title: 'delete(displayed:options:actionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/delete(displayed:options:actionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/delete(displayed:options:actionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/delete%28displayed%3Aoptions%3Aactionhandler%3A%29.json'
content_hash: 'sha256:0b6af018f2baca48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# delete(displayed:options:actionHandler:)

<sub>Type Method</sub>

Creates a delete system accessory with the specified display state, configuration options, and optional action handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func delete(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.DeleteOptions = DeleteOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the delete accessory appears in. This parameter has a default value of [UICellAccessory.DisplayedState.whenEditing](displayedstate/whenediting.md).

- `options` — Configuration options for the delete accessory. See [DeleteOptions](deleteoptions.md) for possible configuration options.

- `actionHandler` — An optional closure that the system calls when a user interacts with the delete accessory.

## Return Value

A configured delete cell accessory. This accessory is a minus sign inside of a circle with the default system red color. This accessory appears on the leading edge of the cell.

## See Also

### Creating a delete accessory

- [DeleteOptions](deleteoptions.md) — Configuration options for a delete accessory.

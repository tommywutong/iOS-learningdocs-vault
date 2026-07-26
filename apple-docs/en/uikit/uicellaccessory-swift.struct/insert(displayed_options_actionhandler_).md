---
title: 'insert(displayed:options:actionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/insert(displayed:options:actionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/insert(displayed:options:actionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/insert%28displayed%3Aoptions%3Aactionhandler%3A%29.json'
content_hash: 'sha256:521d5d51c9882060'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# insert(displayed:options:actionHandler:)

<sub>Type Method</sub>

Creates an insert system accessory with the specified display state, configuration options, and optional action handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func insert(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.InsertOptions = InsertOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the insert accessory appears in. This parameter has a default value of [UICellAccessory.DisplayedState.whenEditing](displayedstate/whenediting.md).

- `options` — Configuration options for the insert accessory. See [InsertOptions](insertoptions.md) for possible configuration options.

- `actionHandler` — An optional closure that the system calls when a user interacts with the insert accessory.

## Return Value

A configured insert cell accessory. This accessory is a plus sign inside of a circle with the default system green color. This accessory appears on the leading edge of the cell.

## See Also

### Creating an insert accessory

- [InsertOptions](insertoptions.md) — Configuration options for an insert accessory.

---
title: 'detail(displayed:options:actionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, tvOS 15.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/detail(displayed:options:actionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/detail(displayed:options:actionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/detail%28displayed%3Aoptions%3Aactionhandler%3A%29.json'
content_hash: 'sha256:303a8ec08dd06c31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# detail(displayed:options:actionHandler:)

<sub>Type Method</sub>

Creates a detail system accessory with the specified display state, configuration options, and optional action handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func detail(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.DetailOptions = DetailOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the detail accessory appears in. This parameter has a default value of [UICellAccessory.DisplayedState.always](displayedstate/always.md).

- `options` — Configuration options for the detail accessory. See [DetailOptions](detailoptions.md) for possible configuration options.

- `actionHandler` — An optional closure that the system calls when a user interacts with the detail accessory.

## Return Value

A configured detail cell accessory. The accessory displays as the system information button. This accessory appears on the trailing edge of the cell.

## See Also

### Creating a detail accessory

- [DetailOptions](detailoptions.md) — Configuration options for a detail accessory.

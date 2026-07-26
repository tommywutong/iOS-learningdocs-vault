---
title: 'outlineDisclosure(displayed:options:actionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosure(displayed:options:actionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosure(displayed:options:actionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosure%28displayed%3Aoptions%3Aactionhandler%3A%29.json'
content_hash: 'sha256:e8a56e51f0381ba2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# outlineDisclosure(displayed:options:actionHandler:)

<sub>Type Method</sub>

Creates an outline disclosure system accessory with the specified display state, configuration options, and optional action handler.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func outlineDisclosure(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.OutlineDisclosureOptions = OutlineDisclosureOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the outline disclosure appears in. This parameter has a default value of [UICellAccessory.DisplayedState.always](displayedstate/always.md).

- `options` — Configuration options for the outline disclosure. See [OutlineDisclosureOptions](outlinedisclosureoptions.md) for possible configuration options.

- `actionHandler` — An optional closure that the system calls when a user interacts with the outline disclosure.

## Return Value

A configured outline disclosure cell accessory. This accessory is a rotating chevron for use in outlines. In iOS and for headers in Mac Catalyst, this accessory appears on the trailing edge. For cells in Mac Catalyst, this accessory appears on the leading edge.

## Discussion

Use this cell accessory to indicate that an item can expand and collapse, and to enable the user to toggle between the expanded and collapsed states.

## See Also

### Creating an outline disclosure

- [OutlineDisclosureOptions](outlinedisclosureoptions.md) — Configuration options for an outline disclosure.

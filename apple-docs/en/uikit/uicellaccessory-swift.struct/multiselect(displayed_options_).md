---
title: 'multiselect(displayed:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/multiselect(displayed:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/multiselect(displayed:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/multiselect%28displayed%3Aoptions%3A%29.json'
content_hash: 'sha256:9210dd60f0f576d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# multiselect(displayed:options:)

<sub>Type Method</sub>

Creates a multiselect system accessory with the specified display state and configuration options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func multiselect(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.MultiselectOptions = MultiselectOptions()) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the multiselect accessory appears in. This parameter has a default value of [UICellAccessory.DisplayedState.whenEditing](displayedstate/whenediting.md).

- `options` — Configuration options for the multiselect accessory. See [MultiselectOptions](multiselectoptions.md) for possible configuration options.

## Return Value

A configured multiselect cell accessory that changes apperance according to the cell’s selection state. The accessory displays as an empty circle for an unselected cell and as a filled circle with a checkmark for a selected cell. This accessory appears on the leading edge of the cell.

## See Also

### Creating a multiselect accessory

- [MultiselectOptions](multiselectoptions.md) — Configuration options for a multiselect accessory.

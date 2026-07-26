---
title: 'label(text:displayed:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/label(text:displayed:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/label(text:displayed:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/label%28text%3Adisplayed%3Aoptions%3A%29.json'
content_hash: 'sha256:0d8b4a2903ceaf2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# label(text:displayed:options:)

<sub>Type Method</sub>

Creates a label system accessory with the specified text, display state, and configuration options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func label(text: String, displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.LabelOptions = LabelOptions()) -> UICellAccessory
```

## Parameters

- `text` — The text for the label to display.

- `displayed` — The cell-editing states that the label accessory appears in. This parameter has a default value of [UICellAccessory.DisplayedState.always](displayedstate/always.md).

- `options` — Configuration options for the label. See [LabelOptions](labeloptions.md) for possible configuration options.

## Return Value

A configured label cell accessory. This accessory appears on the trailing edge of the cell.

## Discussion

Use this cell accessory to display a short string of text, like a small number showing the count for the associated item.

## See Also

### Creating a label accessory

- [LabelOptions](labeloptions.md) — Configuration options for a label accessory.

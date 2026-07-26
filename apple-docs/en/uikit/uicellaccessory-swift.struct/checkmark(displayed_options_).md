---
title: 'checkmark(displayed:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/checkmark(displayed:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/checkmark(displayed:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/checkmark%28displayed%3Aoptions%3A%29.json'
content_hash: 'sha256:1f2be55598e054bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# checkmark(displayed:options:)

<sub>Type Method</sub>

Creates a checkmark system accessory with the specified display state and configuration options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func checkmark(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.CheckmarkOptions = CheckmarkOptions()) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the checkmark appears in. This parameter has a default value of [UICellAccessory.DisplayedState.always](displayedstate/always.md).

- `options` — Configuration options for the checkmark. See [CheckmarkOptions](checkmarkoptions.md) for possible configuration options.

## Return Value

A configured checkmark cell accessory. This accessory is a checkmark with the default system green color. This accessory appears on the trailing edge of the cell.

## See Also

### Creating a checkmark accessory

- [CheckmarkOptions](checkmarkoptions.md) — Configuration options for a checkmark accessory.

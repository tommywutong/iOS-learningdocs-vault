---
title: 'reorder(displayed:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/reorder(displayed:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/reorder(displayed:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/reorder%28displayed%3Aoptions%3A%29.json'
content_hash: 'sha256:cc1612aa2e67c69f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# reorder(displayed:options:)

<sub>Type Method</sub>

Creates a reorder system accessory with the specified display state and configuration options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func reorder(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.ReorderOptions = ReorderOptions()) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the reorder accessory appears in. This parameter has a default value of [UICellAccessory.DisplayedState.whenEditing](displayedstate/whenediting.md).

- `options` — Configuration options for the reorder accessory. See [ReorderOptions](reorderoptions.md) for possible configuration options.

## Return Value

A configured reorder cell accessory. This accessory is three horizontal lines with the default system gray color. This accessory appears on the trailing edge of the cell.

## Discussion

If your collection view supports interactive reordering of its cells, a user can drag the cell by its reorder accessory to change the order of the cell in the collection view.

## See Also

### Creating a reorder accessory

- [ReorderOptions](reorderoptions.md) — Configuration options for a reorder accessory.

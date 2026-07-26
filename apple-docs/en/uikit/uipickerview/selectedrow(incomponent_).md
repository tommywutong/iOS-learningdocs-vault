---
title: 'selectedRow(inComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerview/selectedrow(incomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/selectedrow(incomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/selectedrow%28incomponent%3A%29.json'
content_hash: 'sha256:2a7a900b81aaec60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# selectedRow(inComponent:)

<sub>Instance Method</sub>

Returns the index of the selected row in a given component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func selectedRow(inComponent component: Int) -> Int
```

## Parameters

- `component` — A zero-indexed number identifying a component of the picker view.

## Return Value

A zero-indexed number identifying the selected row, or `-1` if no row is selected.

## See Also

### Selecting rows in the view picker

- [- selectRow:inComponent:animated:](<selectrow(__incomponent_animated_).md>) — Selects a row in a specified component of the picker view.

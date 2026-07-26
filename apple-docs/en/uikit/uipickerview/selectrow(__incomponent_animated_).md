---
title: 'selectRow(_:inComponent:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerview/selectrow(_:incomponent:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/selectrow(_:incomponent:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/selectrow%28_%3Aincomponent%3Aanimated%3A%29.json'
content_hash: 'sha256:fcc066915fb544b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# selectRow(_:inComponent:animated:)

<sub>Instance Method</sub>

Selects a row in a specified component of the picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func selectRow(_ row: Int, inComponent component: Int, animated: Bool)
```

## Parameters

- `row` — A zero-indexed number identifying a row of `component`.

- `component` — A zero-indexed number identifying a component of the picker view.

- `animated` — [true](../../swift/true.md) to animate the selection by spinning the wheel (component) to the new value; if you specify [false](../../swift/false.md), the new selection is shown immediately.

## See Also

### Selecting rows in the view picker

- [- selectedRowInComponent:](<selectedrow(incomponent_).md>) — Returns the index of the selected row in a given component.

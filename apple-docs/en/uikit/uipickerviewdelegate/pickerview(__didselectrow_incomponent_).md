---
title: 'pickerView(_:didSelectRow:inComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdelegate/pickerview(_:didselectrow:incomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:didselectrow:incomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdelegate/pickerview%28_%3Adidselectrow%3Aincomponent%3A%29.json'
content_hash: 'sha256:c272cef202c61f79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDelegate](../uipickerviewdelegate.md)

# pickerView(_:didSelectRow:inComponent:)

<sub>Instance Method</sub>

Called by the picker view when the user selects a row in a component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int)
```

## Parameters

- `pickerView` — An object representing the picker view requesting the data.

- `row` — A zero-indexed number identifying a row of `component`. Rows are numbered top-to-bottom.

- `component` — A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

## Discussion

To determine what value the user selected, the delegate uses the `row` index to access the value at the corresponding position in the array used to construct the component.

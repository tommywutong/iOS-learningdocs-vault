---
title: 'pickerView(_:rowHeightForComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdelegate/pickerview(_:rowheightforcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:rowheightforcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdelegate/pickerview%28_%3Arowheightforcomponent%3A%29.json'
content_hash: 'sha256:7515208529f7b1a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDelegate](../uipickerviewdelegate.md)

# pickerView(_:rowHeightForComponent:)

<sub>Instance Method</sub>

Called by the picker view when it needs the row height to use for drawing row content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, rowHeightForComponent component: Int) -> CGFloat
```

## Parameters

- `pickerView` — The picker view requesting this information.

- `component` — A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

## Return Value

A float value indicating the height of the row in points.

## See Also

### Setting the dimensions of the picker view

- [- pickerView:widthForComponent:](<pickerview(__widthforcomponent_).md>) — Called by the picker view when it needs the row width to use for drawing row content.

---
title: 'pickerView(_:widthForComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdelegate/pickerview(_:widthforcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:widthforcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdelegate/pickerview%28_%3Awidthforcomponent%3A%29.json'
content_hash: 'sha256:33e2337ed020ff2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDelegate](../uipickerviewdelegate.md)

# pickerView(_:widthForComponent:)

<sub>Instance Method</sub>

Called by the picker view when it needs the row width to use for drawing row content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, widthForComponent component: Int) -> CGFloat
```

## Parameters

- `pickerView` — The picker view requesting this information.

- `component` — A zero-indexed number identifying a component of the picker view. Components are numbered left-to-right.

## Return Value

A float value indicating the width of the row in points.

## See Also

### Setting the dimensions of the picker view

- [- pickerView:rowHeightForComponent:](<pickerview(__rowheightforcomponent_).md>) — Called by the picker view when it needs the row height to use for drawing row content.

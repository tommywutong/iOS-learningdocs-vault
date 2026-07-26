---
title: 'pickerView(_:viewForRow:forComponent:reusing:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdelegate/pickerview(_:viewforrow:forcomponent:reusing:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:viewforrow:forcomponent:reusing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdelegate/pickerview%28_%3Aviewforrow%3Aforcomponent%3Areusing%3A%29.json'
content_hash: 'sha256:006b79bf00623290'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDelegate](../uipickerviewdelegate.md)

# pickerView(_:viewForRow:forComponent:reusing:)

<sub>Instance Method</sub>

Called by the picker view when it needs the view to use for a given row in a given component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusing view: UIView?) -> UIView
```

## Parameters

- `pickerView` — An object representing the picker view requesting the data.

- `row` — A zero-indexed number identifying a row of `component`. Rows are numbered top-to-bottom.

- `component` — A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

- `view` — A view object that was previously used for this row, but is now hidden and cached by the picker view.

## Return Value

A view object to use as the content of `row`. The object can be any subclass of [UIView](../uiview.md), such as [UILabel](../uilabel.md), [UIImageView](../uiimageview.md), or even a custom view.

## Discussion

If the previously used view (the `view` parameter) is adequate, return that. If you return a different view, the previously used view is released. The picker view centers the returned view in the rectangle for `row`.

## See Also

### Setting the content of component rows

- [- pickerView:titleForRow:forComponent:](<pickerview(__titleforrow_forcomponent_).md>) — Called by the picker view when it needs the title to use for a given row in a given component.
- [- pickerView:attributedTitleForRow:forComponent:](<pickerview(__attributedtitleforrow_forcomponent_).md>) — Called by the picker view when it needs the styled title to use for a given row in a given component.

---
title: 'pickerView(_:titleForRow:forComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdelegate/pickerview(_:titleforrow:forcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:titleforrow:forcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdelegate/pickerview%28_%3Atitleforrow%3Aforcomponent%3A%29.json'
content_hash: 'sha256:a746e630a78a0ce5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDelegate](../uipickerviewdelegate.md)

# pickerView(_:titleForRow:forComponent:)

<sub>Instance Method</sub>

Called by the picker view when it needs the title to use for a given row in a given component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String?
```

## Parameters

- `pickerView` — An object representing the picker view requesting the data.

- `row` — A zero-indexed number identifying a row of `component`. Rows are numbered top-to-bottom.

- `component` — A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

## Return Value

The string to use as the title of the indicated component row.

## Discussion

If you implement both this method and the [- pickerView:attributedTitleForRow:forComponent:](<pickerview(__attributedtitleforrow_forcomponent_).md>) method, the picker view prefers the [- pickerView:attributedTitleForRow:forComponent:](<pickerview(__attributedtitleforrow_forcomponent_).md>) method. However, if that method returns `nil`, the picker view falls back to using the string returned by this method.

## See Also

### Setting the content of component rows

- [- pickerView:attributedTitleForRow:forComponent:](<pickerview(__attributedtitleforrow_forcomponent_).md>) — Called by the picker view when it needs the styled title to use for a given row in a given component.
- [- pickerView:viewForRow:forComponent:reusingView:](<pickerview(__viewforrow_forcomponent_reusing_).md>) — Called by the picker view when it needs the view to use for a given row in a given component.

---
title: 'pickerView(_:attributedTitleForRow:forComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdelegate/pickerview%28_%3Aattributedtitleforrow%3Aforcomponent%3A%29.json'
content_hash: 'sha256:5eeb403459b062e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDelegate](../uipickerviewdelegate.md)

# pickerView(_:attributedTitleForRow:forComponent:)

<sub>Instance Method</sub>

Called by the picker view when it needs the styled title to use for a given row in a given component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, attributedTitleForRow row: Int, forComponent component: Int) -> NSAttributedString?
```

## Parameters

- `pickerView` — An object representing the picker view requesting the data.

- `row` — A zero-indexed number identifying a row of `component`. Rows are numbered top-to-bottom.

- `component` — A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

## Return Value

The attributed string to use as the title of the indicated component row.

## Discussion

If you implement both this method and the [- pickerView:titleForRow:forComponent:](<pickerview(__titleforrow_forcomponent_).md>) method, the picker view prefers the use of this method. However, if your implementation of this method returns `nil`, the picker view falls back to using the string returned by the [- pickerView:titleForRow:forComponent:](<pickerview(__titleforrow_forcomponent_).md>) method.

## See Also

### Setting the content of component rows

- [- pickerView:titleForRow:forComponent:](<pickerview(__titleforrow_forcomponent_).md>) — Called by the picker view when it needs the title to use for a given row in a given component.
- [- pickerView:viewForRow:forComponent:reusingView:](<pickerview(__viewforrow_forcomponent_reusing_).md>) — Called by the picker view when it needs the view to use for a given row in a given component.

---
title: 'view(forRow:forComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerview/view(forrow:forcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/view(forrow:forcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/view%28forrow%3Aforcomponent%3A%29.json'
content_hash: 'sha256:c5b03cf7a672f311'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# view(forRow:forComponent:)

<sub>Instance Method</sub>

Returns the view used by the picker view for a given row and component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func view(forRow row: Int, forComponent component: Int) -> UIView?
```

## Parameters

- `row` — The zero-indexed number of a row of the picker view.

- `component` — The zero-indexed number of a component of the picker view.

## Return Value

The view provided by the delegate in the [- pickerView:viewForRow:forComponent:reusingView:](<../uipickerviewdelegate/pickerview(__viewforrow_forcomponent_reusing_).md>) method. Returns `nil` if the specified row of the component is not visible or if the delegate does not implement p`ickerView:viewForRow:forComponent:reusingView:`.

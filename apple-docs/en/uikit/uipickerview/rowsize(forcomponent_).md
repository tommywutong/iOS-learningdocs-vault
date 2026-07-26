---
title: 'rowSize(forComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerview/rowsize(forcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/rowsize(forcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/rowsize%28forcomponent%3A%29.json'
content_hash: 'sha256:d773832beb4a7c44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# rowSize(forComponent:)

<sub>Instance Method</sub>

Returns the size of a row for a component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func rowSize(forComponent component: Int) -> CGSize
```

## Parameters

- `component` — A zero-indexed number identifying a component.

## Return Value

The size of rows in the given component. This is generally the size required to display the largest string or view used as a row in the component.

## Discussion

A picker view fetches the value of this property by calling the [- pickerView:widthForComponent:](<../uipickerviewdelegate/pickerview(__widthforcomponent_).md>) and [- pickerView:rowHeightForComponent:](<../uipickerviewdelegate/pickerview(__rowheightforcomponent_).md>) delegate methods, and caches it. The default value is (`0`, `0`).

## See Also

### Getting the dimensions of the picker view

- [numberOfComponents](numberofcomponents.md) — The number of components for the picker view.
- [- numberOfRowsInComponent:](<numberofrows(incomponent_).md>) — Returns the number of rows for a component.

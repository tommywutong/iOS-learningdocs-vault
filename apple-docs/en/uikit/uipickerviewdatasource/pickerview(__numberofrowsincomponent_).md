---
title: 'pickerView(_:numberOfRowsInComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdatasource/pickerview(_:numberofrowsincomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdatasource/pickerview(_:numberofrowsincomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdatasource/pickerview%28_%3Anumberofrowsincomponent%3A%29.json'
content_hash: 'sha256:ac650a0f0c38da75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDataSource](../uipickerviewdatasource.md)

# pickerView(_:numberOfRowsInComponent:)

<sub>Instance Method</sub>

Asks the data source for the number of rows for a specified component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int
```

## Parameters

- `pickerView` — The picker view requesting the data.

- `component` — A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

## Return Value

The number of rows for the component.

## See Also

### Providing counts for the picker view

- [- numberOfComponentsInPickerView:](<numberofcomponents(in_).md>) — Asks the data source for the number of components in the picker view.

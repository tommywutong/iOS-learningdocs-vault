---
title: 'numberOfComponents(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewdatasource/numberofcomponents(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdatasource/numberofcomponents(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdatasource/numberofcomponents%28in%3A%29.json'
content_hash: 'sha256:14d581481a1bd854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewDataSource](../uipickerviewdatasource.md)

# numberOfComponents(in:)

<sub>Instance Method</sub>

Asks the data source for the number of components in the picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func numberOfComponents(in pickerView: UIPickerView) -> Int
```

## Parameters

- `pickerView` — The picker view requesting the data.

## Return Value

The number of components (or “columns”) that the picker view should display.

## See Also

### Providing counts for the picker view

- [- pickerView:numberOfRowsInComponent:](<pickerview(__numberofrowsincomponent_).md>) — Asks the data source for the number of rows for a specified component.

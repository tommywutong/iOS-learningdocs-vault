---
title: dataSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerview/datasource
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/datasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/datasource.json'
content_hash: 'sha256:83b0618d8ef93f78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# dataSource

<sub>Instance Property</sub>

The data source for the picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var dataSource: (any UIPickerViewDataSource)? { get set }
```

## Discussion

The data source must adopt the [UIPickerViewDataSource](../uipickerviewdatasource.md) protocol and implement the required methods to return the number of components and the number of rows in each component.

## See Also

### Providing the picker data

- [UIPickerViewDataSource](../uipickerviewdatasource.md) — The interface for a picker view’s data source.

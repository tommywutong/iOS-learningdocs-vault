---
title: 'numberOfRows(inComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerview/numberofrows(incomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/numberofrows(incomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/numberofrows%28incomponent%3A%29.json'
content_hash: 'sha256:59d4b189cf098e47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# numberOfRows(inComponent:)

<sub>Instance Method</sub>

Returns the number of rows for a component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func numberOfRows(inComponent component: Int) -> Int
```

## Parameters

- `component` — A zero-indexed number identifying a component.

## Return Value

The number of rows in the given component.

## Discussion

A picker view fetches the value of this property from the data source and and caches it. The default value is zero.

## See Also

### Getting the dimensions of the picker view

- [numberOfComponents](numberofcomponents.md) — The number of components for the picker view.
- [- rowSizeForComponent:](<rowsize(forcomponent_).md>) — Returns the size of a row for a component.

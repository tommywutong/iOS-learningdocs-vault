---
title: numberOfComponents
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerview/numberofcomponents
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/numberofcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/numberofcomponents.json'
content_hash: 'sha256:318c8525b7de68d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# numberOfComponents

<sub>Instance Property</sub>

The number of components for the picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var numberOfComponents: Int { get }
```

## Discussion

A [UIPickerView](../uipickerview.md) object fetches the value of this property from the data source and caches it. The default value is `0`.

## See Also

### Getting the dimensions of the picker view

- [- numberOfRowsInComponent:](<numberofrows(incomponent_).md>) — Returns the number of rows for a component.
- [- rowSizeForComponent:](<rowsize(forcomponent_).md>) — Returns the size of a row for a component.

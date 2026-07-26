---
title: 'numberOfRows(inSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/numberofrows(insection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/numberofrows(insection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/numberofrows%28insection%3A%29.json'
content_hash: 'sha256:6da2a1dfb99f3a09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# numberOfRows(inSection:)

<sub>Instance Method</sub>

Returns the number of rows (table cells) in a specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func numberOfRows(inSection section: Int) -> Int
```

## Parameters

- `section` — An index number that identifies a section of the table. Table views in a plain style have a section index of zero.

## Return Value

The number of rows in the section.

## Discussion

[UITableView](../uitableview.md) gets the value returned by this method from its data source and caches it.

## See Also

### Getting the number of rows and sections

- [numberOfSections](numberofsections.md) — The number of sections in the table view.

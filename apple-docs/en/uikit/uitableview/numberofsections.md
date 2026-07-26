---
title: numberOfSections
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/numberofsections
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/numberofsections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/numberofsections.json'
content_hash: 'sha256:3c1cca8d31ed610c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# numberOfSections

<sub>Instance Property</sub>

The number of sections in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var numberOfSections: Int { get }
```

## Discussion

[UITableView](../uitableview.md) gets the value in this property from its data source and caches it.

## See Also

### Getting the number of rows and sections

- [- numberOfRowsInSection:](<numberofrows(insection_).md>) — Returns the number of rows (table cells) in a specified section.

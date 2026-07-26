---
title: 'rectForRow(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/rectforrow(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/rectforrow(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/rectforrow%28at%3A%29.json'
content_hash: 'sha256:a09b4abab7c5db52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# rectForRow(at:)

<sub>Instance Method</sub>

Returns the drawing area for a row that an index path identifies.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func rectForRow(at indexPath: IndexPath) -> CGRect
```

## Parameters

- `indexPath` — An index path object that identifies a row by its index and its section index.

## Return Value

A rectangle defining the area in which the table view draws the row or [CGRectZero](../../coregraphics/cgrectzero.md) if `indexPath` is invalid.

## See Also

### Getting the drawing areas for the table

- [- rectForSection:](<rect(forsection_).md>) — Returns the drawing area for a specified section of the table view.
- [- rectForFooterInSection:](<rectforfooter(insection_).md>) — Returns the drawing area for the footer of the specified section.
- [- rectForHeaderInSection:](<rectforheader(insection_).md>) — Returns the drawing area for the header of the specified section.

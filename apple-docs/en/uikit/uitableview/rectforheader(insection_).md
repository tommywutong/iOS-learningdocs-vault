---
title: 'rectForHeader(inSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/rectforheader(insection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/rectforheader(insection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/rectforheader%28insection%3A%29.json'
content_hash: 'sha256:72f5ef86f693d273'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# rectForHeader(inSection:)

<sub>Instance Method</sub>

Returns the drawing area for the header of the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func rectForHeader(inSection section: Int) -> CGRect
```

## Parameters

- `section` — An index number identifying a section of the table view. Plain-style table views always have a section index of zero.

## Return Value

A rectangle defining the area in which the table view draws the section header.

## See Also

### Getting the drawing areas for the table

- [- rectForSection:](<rect(forsection_).md>) — Returns the drawing area for a specified section of the table view.
- [- rectForRowAtIndexPath:](<rectforrow(at_).md>) — Returns the drawing area for a row that an index path identifies.
- [- rectForFooterInSection:](<rectforfooter(insection_).md>) — Returns the drawing area for the footer of the specified section.

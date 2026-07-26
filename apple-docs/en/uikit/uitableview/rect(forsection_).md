---
title: 'rect(forSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/rect(forsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/rect(forsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/rect%28forsection%3A%29.json'
content_hash: 'sha256:415d3bb346428de1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# rect(forSection:)

<sub>Instance Method</sub>

Returns the drawing area for a specified section of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func rect(forSection section: Int) -> CGRect
```

## Parameters

- `section` — An index number identifying a section of the table view. Plain-style table views always have a section index of zero.

## Return Value

A rectangle defining the area in which the table view draws the section.

## See Also

### Getting the drawing areas for the table

- [- rectForRowAtIndexPath:](<rectforrow(at_).md>) — Returns the drawing area for a row that an index path identifies.
- [- rectForFooterInSection:](<rectforfooter(insection_).md>) — Returns the drawing area for the footer of the specified section.
- [- rectForHeaderInSection:](<rectforheader(insection_).md>) — Returns the drawing area for the header of the specified section.

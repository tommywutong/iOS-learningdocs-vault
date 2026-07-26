---
title: accessibilityRowRange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilityrowrange()
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilityrowrange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilityrowrange%28%29.json'
content_hash: 'sha256:d1dd5341a123da26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityContainerDataTableCell](../uiaccessibilitycontainerdatatablecell.md)

# accessibilityRowRange()

<sub>Instance Method</sub>

Returns the visible range of rows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func accessibilityRowRange() -> NSRange
```

## Return Value

The visible range of rows.

## Discussion

Set the location of the range to the first row containing the cell. Use the length of the range to specify the number of rows that the cell spans. If you do not implement this method, the system assumes an initial index of [NSNotFound](../../foundation/nsnotfound-9t5v2.md) and a length of `0`.

## See Also

### Getting the rows and columns

- [- accessibilityColumnRange](<accessibilitycolumnrange().md>) — Returns the columns spanned by the cell.

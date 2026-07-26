---
title: accessibilityColumnRange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilitycolumnrange()
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilitycolumnrange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilitycolumnrange%28%29.json'
content_hash: 'sha256:df07567ca7a58eb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityContainerDataTableCell](../uiaccessibilitycontainerdatatablecell.md)

# accessibilityColumnRange()

<sub>Instance Method</sub>

Returns the columns spanned by the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func accessibilityColumnRange() -> NSRange
```

## Return Value

The column or columns that the cell spans.

## Discussion

Set the location of the range to the first column containing the cell. Use the length of the range to specify the number of columns that the cell spans. If you do not implement this method, the system assumes an initial index of [NSNotFound](../../foundation/nsnotfound-9t5v2.md) and a length of `0`.

## See Also

### Getting the rows and columns

- [- accessibilityRowRange](<accessibilityrowrange().md>) — Returns the visible range of rows.

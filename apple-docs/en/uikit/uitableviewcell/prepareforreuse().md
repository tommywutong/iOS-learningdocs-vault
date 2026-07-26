---
title: prepareForReuse()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/prepareforreuse()
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/prepareforreuse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/prepareforreuse%28%29.json'
content_hash: 'sha256:a239688dafd31774'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# prepareForReuse()

<sub>Instance Method</sub>

Prepares a reusable cell for reuse by the table view’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepareForReuse()
```

## Discussion

If a [UITableViewCell](../uitableviewcell.md) object has a reuse identifier, the table view invokes this method just before returning the object from the `UITableView` method [- dequeueReusableCellWithIdentifier:](<../uitableview/dequeuereusablecell(withidentifier_).md>). To avoid potential performance issues, you should only reset attributes of the cell that are not related to content, for example, alpha, editing, and selection state. The table view’s delegate in [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>) should _always_ reset all content when reusing a cell.

The table view doesn’t call this method if the cell object doesn’t have an associated reuse identifier, or if you use [- reconfigureRowsAtIndexPaths:](<../uitableview/reconfigurerows(at_).md>) to update the contents of an existing cell.

If you override this method, you must be sure to invoke the superclass implementation.

## See Also

### Reusing cells

- [reuseIdentifier](reuseidentifier.md) — A string for identifying a reusable cell.

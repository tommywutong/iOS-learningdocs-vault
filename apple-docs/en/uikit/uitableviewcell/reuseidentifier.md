---
title: reuseIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/reuseidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/reuseidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/reuseidentifier.json'
content_hash: 'sha256:a34152bc61086eff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# reuseIdentifier

<sub>Instance Property</sub>

A string for identifying a reusable cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var reuseIdentifier: String? { get }
```

## Discussion

The reuse identifier is associated with a [UITableViewCell](../uitableviewcell.md) object that the table-view’s delegate creates with the intent to reuse it as the basis (for performance reasons) for multiple rows of a table view. It is assigned to the cell object in [initWithFrame:reuseIdentifier:](initwithframe_reuseidentifier_.md) and cannot be changed thereafter. A [UITableView](../uitableview.md) object maintains a queue (or list) of the currently reusable cells, each with its own reuse identifier, and makes them available to the delegate in the [- dequeueReusableCellWithIdentifier:](<../uitableview/dequeuereusablecell(withidentifier_).md>) method.

## See Also

### Reusing cells

- [- prepareForReuse](<prepareforreuse().md>) — Prepares a reusable cell for reuse by the table view’s delegate.

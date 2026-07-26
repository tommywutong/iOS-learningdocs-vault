---
title: nextFocusedIndexPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewfocusupdatecontext/nextfocusedindexpath
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/nextfocusedindexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewfocusupdatecontext/nextfocusedindexpath.json'
content_hash: 'sha256:f5ad8779b50d3402'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewFocusUpdateContext](../uitableviewfocusupdatecontext.md)

# nextFocusedIndexPath

<sub>Instance Property</sub>

Returns the index path of the cell containing the context’s next focused view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var nextFocusedIndexPath: IndexPath? { get }
```

## Discussion

This property returns the index path only when the [nextFocusedView](../uifocusupdatecontext/nextfocusedview.md) is located within a cell of the table view. Otherwise, it returns `nil`. This can happen if focus is moving out of the table view, because the [nextFocusedView](../uifocusupdatecontext/nextfocusedview.md) isn’t associated with an index path in this table view.

When focus is moving from one table view to another, each table view delegate is called with [previouslyFocusedIndexPath](previouslyfocusedindexpath.md) and [nextFocusedIndexPath](nextfocusedindexpath.md) configured for its specific table view.

## See Also

### Locating focusable items in a table view

- [previouslyFocusedIndexPath](previouslyfocusedindexpath.md) — Returns the index path of the cell containing the context’s previously focused view.

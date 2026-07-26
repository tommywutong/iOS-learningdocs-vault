---
title: previouslyFocusedIndexPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewfocusupdatecontext/previouslyfocusedindexpath
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/previouslyfocusedindexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewfocusupdatecontext/previouslyfocusedindexpath.json'
content_hash: 'sha256:98b76c4af5193744'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewFocusUpdateContext](../uitableviewfocusupdatecontext.md)

# previouslyFocusedIndexPath

<sub>Instance Property</sub>

Returns the index path of the cell containing the context’s previously focused view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var previouslyFocusedIndexPath: IndexPath? { get }
```

## Discussion

This property returns the index path only when the [previouslyFocusedView](../uifocusupdatecontext/previouslyfocusedview.md) is located within a cell of the table view. Otherwise, it returns `nil`. This can happen if focus is moving into the table view, because the [previouslyFocusedView](../uifocusupdatecontext/previouslyfocusedview.md) isn’t associated with an index path in this table view.

When focus is moving from one table view to another, each table view delegate is called with [previouslyFocusedIndexPath](previouslyfocusedindexpath.md) and [nextFocusedIndexPath](nextfocusedindexpath.md) configured for its specific table view.

## See Also

### Locating focusable items in a table view

- [nextFocusedIndexPath](nextfocusedindexpath.md) — Returns the index path of the cell containing the context’s next focused view.

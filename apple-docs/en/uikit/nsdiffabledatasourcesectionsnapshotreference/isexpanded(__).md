---
title: 'isExpanded(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/isexpanded(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/isexpanded(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/isexpanded%28_%3A%29.json'
content_hash: 'sha256:37949443ee2e2ff2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshotReference](../nsdiffabledatasourcesectionsnapshotreference.md)

# isExpanded(_:)

<sub>Instance Method</sub>

Indicates whether the item with the specified identifier is in an expanded state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func isExpanded(_ item: Any) -> Bool
```

## Discussion

This expansion state persists along with the section snapshot.

## See Also

### Expanding and collapsing items

- [- expandItems:](<expanditems(__).md>) — Expands the specified items in the section snapshot.
- [- collapseItems:](<collapseitems(__).md>) — Collapses the specified items in the section snapshot.

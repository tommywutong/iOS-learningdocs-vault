---
title: 'insert(_:beforeItem:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/insert(_:beforeitem:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/insert(_:beforeitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/insert%28_%3Abeforeitem%3A%29.json'
content_hash: 'sha256:d8fa4d55e06118e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshotReference](../nsdiffabledatasourcesectionsnapshotreference.md)

# insert(_:beforeItem:)

<sub>Instance Method</sub>

Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insert(_ snapshot: NSDiffableDataSourceSectionSnapshotReference, beforeItem item: Any)
```

## See Also

### Inserting items

- [- insertSnapshot:afterItem:](<insert(__afteritem_).md>) — Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [- insertItems:afterItem:](<insertitems(__afteritem_).md>) — Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [- insertItems:beforeItem:](<insertitems(__beforeitem_).md>) — Inserts the provided items immediately before the item with the specified identifier in the section snapshot.

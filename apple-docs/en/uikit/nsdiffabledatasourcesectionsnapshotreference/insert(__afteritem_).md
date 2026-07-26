---
title: 'insert(_:afterItem:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/insert(_:afteritem:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/insert(_:afteritem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/insert%28_%3Aafteritem%3A%29.json'
content_hash: 'sha256:8e62093203987111'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshotReference](../nsdiffabledatasourcesectionsnapshotreference.md)

# insert(_:afterItem:)

<sub>Instance Method</sub>

Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insert(_ snapshot: NSDiffableDataSourceSectionSnapshotReference, afterItem item: Any) -> Any
```

## See Also

### Inserting items

- [- insertItems:afterItem:](<insertitems(__afteritem_).md>) — Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [- insertSnapshot:beforeItem:](<insert(__beforeitem_).md>) — Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.
- [- insertItems:beforeItem:](<insertitems(__beforeitem_).md>) — Inserts the provided items immediately before the item with the specified identifier in the section snapshot.

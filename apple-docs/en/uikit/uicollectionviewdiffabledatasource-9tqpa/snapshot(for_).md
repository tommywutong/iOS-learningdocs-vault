---
title: 'snapshot(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/snapshot(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/snapshot(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/snapshot%28for%3A%29.json'
content_hash: 'sha256:8a9e305011d8cda1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# snapshot(for:)

<sub>Instance Method</sub>

Returns a representation of the current state of the data in the specified section of the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func snapshot(for section: SectionIdentifierType) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>
```

## See Also

### Updating section data

- [apply(_:to:animatingDifferences:completion:)](<apply(__to_animatingdifferences_completion_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [apply(_:to:animatingDifferences:)](<apply(__to_animatingdifferences_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

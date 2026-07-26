---
title: 'apply(_:to:animatingDifferences:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply%28_%3Ato%3Aanimatingdifferences%3A%29.json'
content_hash: 'sha256:7e799e3e4416f554'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# apply(_:to:animatingDifferences:)

<sub>Instance Method</sub>

Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func apply(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to section: SectionIdentifierType, animatingDifferences: Bool = true) async
```

## See Also

### Updating section data

- [snapshot(for:)](<snapshot(for_).md>) — Returns a representation of the current state of the data in the specified section of the collection view.
- [apply(_:to:animatingDifferences:completion:)](<apply(__to_animatingdifferences_completion_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

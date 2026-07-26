---
title: 'apply(_:to:animatingDifferences:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply%28_%3Ato%3Aanimatingdifferences%3Acompletion%3A%29.json'
content_hash: 'sha256:79dd48328fa562e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# apply(_:to:animatingDifferences:completion:)

<sub>Instance Method</sub>

Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func apply(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to section: SectionIdentifierType, animatingDifferences: Bool = true, completion: (() -> Void)? = nil)
```

## See Also

### Updating section data

- [snapshot(for:)](<snapshot(for_).md>) — Returns a representation of the current state of the data in the specified section of the collection view.
- [apply(_:to:animatingDifferences:)](<apply(__to_animatingdifferences_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

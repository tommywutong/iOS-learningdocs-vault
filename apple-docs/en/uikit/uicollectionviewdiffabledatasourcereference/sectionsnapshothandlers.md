---
title: sectionSnapshotHandlers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers.json'
content_hash: 'sha256:a8557a9f273c8cb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# sectionSnapshotHandlers

<sub>Instance Property</sub>

The diffable data source’s handlers for expanding and collapsing items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var sectionSnapshotHandlers: __UICollectionViewDiffableDataSourceSectionSnapshotHandlers { get set }
```

## Discussion

Provide section snapshot handlers to support the expanding or collapsing of items in your collection view.

Use the [snapshotForExpandingParentItemHandler](../uicollectionviewdiffabledatasourcesectionsnapshothandlers/snapshotforexpandingparentitemhandler.md) handler to customize the snapshot that returns when a particular parent item is expanded.

**Swift**

```swift
// Allow every item to be collapsed
dataSource.sectionSnapshotHandlers.shouldCollapseItem = { item in return true }

dataSource.sectionSnapshotHandlers.snapshotForExpandingParent = {
    parent, currentChildSnapshot -> NSDiffableDataSourceSectionSnapshot<String> in
    
    // Return child snapshot for the parent, or just currentChildSnapshot
}
```

**Objective-C**

```objc
// Allow every item to be collapsed.
[dataSource.sectionSnapshotHandlers setShouldCollapseItemHandler:^BOOL(NSString *item) {
    return YES;
}];

[dataSource.sectionSnapshotHandlers setSnapshotForExpandingParentItemHandler:^NSDiffableDataSourceSectionSnapshot<NSString *> * (NSString *parent, NSDiffableDataSourceSectionSnapshot<NSString *> *currentChildSnapshot) {
    // Return child snapshot for the parent, or just currentChildSnapshot.
}];
```

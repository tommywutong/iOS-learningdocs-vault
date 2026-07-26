---
title: PHFetchResultChangeDetails
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchresultchangedetails
source_url: 'https://developer.apple.com/documentation/photos/phfetchresultchangedetails'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresultchangedetails.json'
content_hash: 'sha256:2f88415d1e77ab31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHFetchResultChangeDetails

<sub>Class</sub>

A description of changes that occurred in the set of asset or collection objects listed in a fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHFetchResultChangeDetails<ObjectType> where ObjectType : PHObject
```

## Overview

A [PHFetchResultChangeDetails](phfetchresultchangedetails.md) object provides detailed information about the differences between two fetch results—one that you previously obtained and an updated one that would result if you performed the same fetch again. The change details object provides information useful for updating a UI that lists the contents of a fetch result, such as the indexes of added, removed, and rearranged objects.

### Processing Changes in Order

PhotoKit describes [changedIndexes](phfetchresultchangedetails/changedindexes.md) in the _after_ state, while [UICollectionView](../uikit/uicollectionview.md)w’s [performBatchUpdates(_:completion:)](<../uikit/uicollectionview/performbatchupdates(__completion_).md>) expects them in the _before_ state. As a result, [changedIndexes](phfetchresultchangedetails/changedindexes.md) can’t be used safely inside [performBatchUpdates(_:completion:)](<../uikit/uicollectionview/performbatchupdates(__completion_).md>).

Instead, use [changedIndexes](phfetchresultchangedetails/changedindexes.md) _after_ and outside the [performBatchUpdates(_:completion:)](<../uikit/uicollectionview/performbatchupdates(__completion_).md>) call, reapplying the code used to configure cells in [cellForItem(at:)](<../uikit/uicollectionview/cellforitem(at_).md>) rather than telling [UICollectionView](../uikit/uicollectionview.md) to reload.

**Swift**

```swift
let collectionView = UICollectionView()
let fetchResultChangeDetails = PHFetchResultChangeDetails()
let deletedCollectionIndicesBeforeChanges = IndexSet()
let insertedCollectionIndicesAfterDeletions = IndexSet()
let deletedPhotoPathsBeforeChanges: [IndexPath] = []
let insertedPhotoPathsAfterDeletions: [IndexPath] = []

collectionView.performBatchUpdates({ () -> Void in
    if (!deletedCollectionIndicesBeforeChanges.isEmpty) {
        collectionView.deleteSections(deletedCollectionIndicesBeforeChanges)
    }
    if (!insertedCollectionIndicesAfterDeletions.isEmpty) {
        collectionView.insertSections(insertedCollectionIndicesAfterDeletions)
    }
    if (!deletedPhotoPathsBeforeChanges.isEmpty) {
        collectionView.deleteItems(at: deletedPhotoPathsBeforeChanges)
    }
    if (!insertedPhotoPathsAfterDeletions.isEmpty) {
        collectionView.insertItems(at: insertedPhotoPathsAfterDeletions)
    }
}, completion:nil)

guard let changeIndices = fetchResultChangeDetails.changedIndexes else {
    return
}
for indexSetElem in changeIndices {
    let indexPath = IndexPath(item: indexSetElem, section: 0)
    guard let changedCell = collectionView.cellForItem(at: indexPath) else {
        break
    }
    // ... Configure changedCell here ...
}
```

**Objective-C**

```objc
@property (nonatomic, strong) UICollectionView* collectionView;
// ...
PHFetchResultChangeDetails* fetchResultChangeDetails;
NSIndexSet* deletedCollectionIndicesBeforeChanges;
NSIndexSet* insertedCollectionIndicesAfterDeletions;
NSArray* deletedPhotoPathsBeforeChanges;
NSArray* insertedPhotoPathsAfterDeletions;

[self.collectionView performBatchUpdates:^{
    if (deletedCollectionIndicesBeforeChanges.count > 0) {
        [self.collectionView deleteSections:deletedCollectionIndicesBeforeChanges];
    }
    if (insertedCollectionIndicesAfterDeletions.count > 0) {
        [self.collectionView insertSections:insertedCollectionIndicesAfterDeletions];
    }
    if (deletedPhotoPathsBeforeChanges.count > 0) {
        [self.collectionView deleteItemsAtIndexPaths:deletedPhotoPathsBeforeChanges];
    }
    if (insertedPhotoPathsAfterDeletions) {
        [self.collectionView insertItemsAtIndexPaths:insertedPhotoPathsAfterDeletions];
    }
} completion:nil];

[fetchResultChangeDetails.changedIndexes enumerateIndexesUsingBlock:^(NSUInteger index, BOOL* stop) {
    NSIndexPath* indexPath = [NSIndexPath indexPathWithItem:index inSection:0];
    UICollectionViewCell* changedCell = [self.collectionView cellForItemAtIndexPath:indexPath];
    if (changedCell) {
        // ... Configure changedCell here ...
    }
    // Set *stop = YES to stop iteration early.
}];
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Changed Fetch Result

- [fetchResultBeforeChanges](phfetchresultchangedetails/fetchresultbeforechanges.md) — The original fetch result, without recent changes.
- [fetchResultAfterChanges](phfetchresultchangedetails/fetchresultafterchanges.md) — The current fetch result, incorporating recent changes.

### Getting Change Information

- [hasIncrementalChanges](phfetchresultchangedetails/hasincrementalchanges.md) — A Boolean value that indicates whether changes to the fetch result can be described incrementally.
- [removedIndexes](phfetchresultchangedetails/removedindexes.md) — The indexes from which objects have been removed from the fetch result.
- [removedObjects](phfetchresultchangedetails/removedobjects.md) — The items that have been removed from the fetch result.
- [insertedIndexes](phfetchresultchangedetails/insertedindexes.md) — The indexes where new objects have been inserted in the fetch result.
- [insertedObjects](phfetchresultchangedetails/insertedobjects.md) — The new items that have been inserted in the fetch result.
- [changedIndexes](phfetchresultchangedetails/changedindexes.md) — The indexes of objects in the fetch result whose content or metadata have been updated.
- [changedObjects](phfetchresultchangedetails/changedobjects.md) — The objects in the fetch result whose content or metadata have been updated.
- [hasMoves](phfetchresultchangedetails/hasmoves.md) — A Boolean value that indicates whether objects have been rearranged in the fetch result.
- [- enumerateMovesWithBlock:](<phfetchresultchangedetails/enumeratemoves(__).md>) — Runs the specified block for each case where an object has moved from one index to another in the fetch result.

### Comparing Fetch Results

- [+ changeDetailsFromFetchResult:toFetchResult:changedObjects:](<phfetchresultchangedetails/init(from_to_changedobjects_).md>) — Creates a change details object that summarizes the differences between two fetch results.

### Initializers

- [init(fromFetchResult:toFetchResult:changedObjects:)](<phfetchresultchangedetails/init(fromfetchresult_tofetchresult_changedobjects_).md>)

## See Also

### Observing Library Changes

- [Observing Changes in the Photo Library](../photokit/observing-changes-in-the-photo-library.md) — Register an observer to be notified of changes to the photo library.
- [- registerChangeObserver:](<phphotolibrary/register(__)-6y3b9.md>) — Registers an object to receive messages when objects in the photo library change.
- [- unregisterChangeObserver:](<phphotolibrary/unregisterchangeobserver(__).md>) — Unregisters an object so that it no longer receives change messages.
- [PHPhotoLibraryChangeObserver](phphotolibrarychangeobserver.md) — A protocol to adopt to have the system notify your app of changes to the photo library.
- [PHChange](phchange.md) — A description of a change that occurred in the photo library.
- [PHObjectChangeDetails](phobjectchangedetails.md) — A description of changes that occurred in an asset or collection object.

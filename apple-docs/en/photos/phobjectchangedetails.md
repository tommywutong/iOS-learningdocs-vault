---
title: PHObjectChangeDetails
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phobjectchangedetails
source_url: 'https://developer.apple.com/documentation/photos/phobjectchangedetails'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phobjectchangedetails.json'
content_hash: 'sha256:bd2dbb8c7fd3f7b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHObjectChangeDetails

<sub>Class</sub>

A description of changes that occurred in an asset or collection object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHObjectChangeDetails<ObjectType> where ObjectType : PHObject
```

## Overview

A [PHObjectChangeDetails](phobjectchangedetails.md) object provides detailed information about differences between two states of an asset or collection object—one that you previously obtained and an updated state that would result if you fetched that entity again. You observe changes by adopting the [PHPhotoLibraryChangeObserver](phphotolibrarychangeobserver.md) protocol and registering your observer with the shared [PHPhotoLibrary](phphotolibrary.md) object. When Photos notifies your observer of a change, you get change details by passing the object you’re interested in to the [changeDetailsForObject:](phchange/changedetailsforobject_.md) method.

For an asset collection or collection list, a [PHObjectChangeDetails](phobjectchangedetails.md) object describe changes only to the collection’s properties. If you’re instead interested in changes to the collection’s membership, fetch the collection’s contents and use the [changeDetails(for:)](<phchange/changedetails(for_)-33a6n.md>) method to track changes to the fetch result.

> [!warning] Warning
> Don’t map [changedIndexes](phfetchresultchangedetails/changedindexes.md) directly to [UICollectionView](../uikit/uicollectionview.md) item indices in batch updates. Use these indices to reconfigure the corresponding cells after [performBatchUpdates(_:completion:)](<../uikit/uicollectionview/performbatchupdates(__completion_).md>). [UICollectionView](../uikit/uicollectionview.md) and [UITableView](../uikit/uitableview.md) expect the [changedIndexes](phfetchresultchangedetails/changedindexes.md) to be in the _before_ state, while PhotoKit provides them in the _after_ state, resulting in a crash if your app performs insertions and deletions at the same time as the changes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Changed Object

- [objectBeforeChanges](phobjectchangedetails/objectbeforechanges.md) — An object that reflects the original state of the asset or collection it represents.
- [objectAfterChanges](phobjectchangedetails/objectafterchanges.md) — An object that reflects the current state of the asset or collection it represents.

### Getting Change Information

- [assetContentChanged](phobjectchangedetails/assetcontentchanged.md) — A Boolean value that indicates whether the asset’s photo or video content has changed.
- [objectWasDeleted](phobjectchangedetails/objectwasdeleted.md) — A Boolean value that indicates whether the object has been deleted from the Photos library.

## See Also

### Observing Library Changes

- [Observing Changes in the Photo Library](../photokit/observing-changes-in-the-photo-library.md) — Register an observer to be notified of changes to the photo library.
- [- registerChangeObserver:](<phphotolibrary/register(__)-6y3b9.md>) — Registers an object to receive messages when objects in the photo library change.
- [- unregisterChangeObserver:](<phphotolibrary/unregisterchangeobserver(__).md>) — Unregisters an object so that it no longer receives change messages.
- [PHPhotoLibraryChangeObserver](phphotolibrarychangeobserver.md) — A protocol to adopt to have the system notify your app of changes to the photo library.
- [PHChange](phchange.md) — A description of a change that occurred in the photo library.
- [PHFetchResultChangeDetails](phfetchresultchangedetails.md) — A description of changes that occurred in the set of asset or collection objects listed in a fetch result.

---
title: PHChange
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phchange
source_url: 'https://developer.apple.com/documentation/photos/phchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phchange.json'
content_hash: 'sha256:0f5cc28041e75ee3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHChange

<sub>Class</sub>

A description of a change that occurred in the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHChange
```

## Overview

Photos provides [PHChange](phchange.md) objects to notify your app of changes to the assets and collections managed by the Photos app. To receive change information, adopt the [PHPhotoLibraryChangeObserver](phphotolibrarychangeobserver.md) protocol and register your observer with the shared [PHPhotoLibrary](phphotolibrary.md) object.

After Photos provides a change object, you use its methods to get a change details object. Call the [changeDetailsForObject:](phchange/changedetailsforobject_.md) or [changeDetails(for:)](<phchange/changedetails(for_)-33a6n.md>) method, passing an asset or collection object you’ve previously fetched or a fetch result containing several such objects. The resulting [PHObjectChangeDetails](phobjectchangedetails.md) or [PHFetchResultChangeDetails](phfetchresultchangedetails.md) object describes any changes that have happened to the object or fetch result since you last fetched it.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Change Details

- [changeDetails(for:)](<phchange/changedetails(for_)-33a6n.md>)
- [changeDetails(for:)](<phchange/changedetails(for_)-536rd.md>) — Returns detailed change information for the specified asset or collection.
- [changeDetails(for:)](<phchange/changedetails(for_)-2fne7.md>) — Returns detailed change information for a fetch result.

## See Also

### Observing Library Changes

- [Observing Changes in the Photo Library](../photokit/observing-changes-in-the-photo-library.md) — Register an observer to be notified of changes to the photo library.
- [- registerChangeObserver:](<phphotolibrary/register(__)-6y3b9.md>) — Registers an object to receive messages when objects in the photo library change.
- [- unregisterChangeObserver:](<phphotolibrary/unregisterchangeobserver(__).md>) — Unregisters an object so that it no longer receives change messages.
- [PHPhotoLibraryChangeObserver](phphotolibrarychangeobserver.md) — A protocol to adopt to have the system notify your app of changes to the photo library.
- [PHObjectChangeDetails](phobjectchangedetails.md) — A description of changes that occurred in an asset or collection object.
- [PHFetchResultChangeDetails](phfetchresultchangedetails.md) — A description of changes that occurred in the set of asset or collection objects listed in a fetch result.

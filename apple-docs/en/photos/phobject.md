---
title: PHObject
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phobject
source_url: 'https://developer.apple.com/documentation/photos/phobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phobject.json'
content_hash: 'sha256:bc46b37b3947e0de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHObject

<sub>Class</sub>

The abstract superclass for Photos model objects (assets and collections).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHObject
```

## Overview

You do not create or use instances of this class directly. Instead, work with instances of its concrete subclasses—[PHAsset](phasset.md), [PHAssetCollection](phassetcollection.md), [PHCollectionList](phcollectionlist.md), and [PHObjectPlaceholder](phobjectplaceholder.md).

Because the [PHObject](phobject.md) class implements the [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>) and [hash](../objectivec/nsobjectprotocol/hash.md) methods in terms of its [localIdentifier](phobject/localidentifier.md) property, you can use techniques that depend on these methods to keep track of asset and collection objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [PHAsset](phasset.md), [PHAssetResourceUploadJob](phassetresourceuploadjob.md), [PHCollection](phcollection.md), [PHObjectPlaceholder](phobjectplaceholder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying an Object

- [localIdentifier](phobject/localidentifier.md) — A unique string that persistently identifies the object.

## See Also

### Asset retrieval

- [Fetching Objects and Requesting Changes](../photokit/fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [PHAsset](phasset.md) — A representation of an image, video, or Live Photo in the Photos library.
- [PHAssetCollection](phassetcollection.md) — A representation of a Photos asset grouping, such as a moment, user-created album, or smart album.
- [PHCollection](phcollection.md) — The abstract superclass for Photos asset collections and collection lists.
- [PHCollectionList](phcollectionlist.md) — A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [PHFetchResult](phfetchresult.md) — An ordered list of assets or collections returned from a Photos fetch method.
- [PHFetchOptions](phfetchoptions.md) — A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.

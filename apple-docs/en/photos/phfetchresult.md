---
title: PHFetchResult
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchresult
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult.json'
content_hash: 'sha256:ff0922b8855e82bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHFetchResult

<sub>Class</sub>

An ordered list of assets or collections returned from a Photos fetch method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHFetchResult<ObjectType> where ObjectType : AnyObject
```

## Overview

When you use class methods on the [PHAsset](phasset.md), [PHCollection](phcollection.md), [PHAssetCollection](phassetcollection.md), and [PHCollectionList](phcollectionlist.md) classes to retrieve objects, Photos provides the resulting objects in a fetch result. You access the contents of a fetch result with the same methods and conventions used by the [NSArray](../foundation/nsarray.md) class. Unlike an [NSArray](../foundation/nsarray.md) object, however, a [PHFetchResult](phfetchresult.md) object dynamically loads its contents from the Photos library as needed, providing optimal performance even when handling a large number of results.

A fetch result provides thread-safe access to its contents. After a fetch, the fetch result’s [count](phfetchresult/count.md) value is constant, and all objects in the fetch result keep the same [localIdentifier](phobject/localidentifier.md) value. (To get updated content for a fetch, register a change observer with the shared [PHPhotoLibrary](phphotolibrary.md) object.)

A fetch result caches its contents, keeping a batch of objects around the most recently accessed index. Because objects outside of the batch are no longer cached, accessing these objects results in refetching those objects. This process can result in changes to values previously read from those objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSFastEnumeration](../foundation/nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Querying a Fetch Result

- [- containsObject:](<phfetchresult/contains(__).md>) — Returns whether the specified object is present in the fetch result.
- [count](phfetchresult/count.md) — The number of objects in the fetch result.
- [- countOfAssetsWithMediaType:](<phfetchresult/countofassets(with_).md>) — Returns the number of assets in the fetch result of a specified type.
- [firstObject](phfetchresult/firstobject.md) — The first object in the fetch result.
- [lastObject](phfetchresult/lastobject.md) — The last object in the fetch result.
- [- objectAtIndex:](<phfetchresult/object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<phfetchresult/subscript(__).md>) — Returns the object located at the specified index.
- [- objectsAtIndexes:](<phfetchresult/objects(at_).md>) — Returns an array containing the objects in the fetch result at the indexes in the specified index set.

### Finding Objects in a Fetch Result

- [- indexOfObject:](<phfetchresult/index(of_).md>) — Returns the lowest index whose corresponding object in the fetch result is equal to the specified object.
- [- indexOfObject:inRange:](<phfetchresult/index(of_in_).md>) — Returns the lowest index within the specified range whose corresponding object in the fetch result is equal to the specified object.

### Performing Operations with Objects in a Fetch Result

- [- enumerateObjectsAtIndexes:options:usingBlock:](<phfetchresult/enumerateobjects(at_options_using_).md>) — Executes the specified block using the objects in the fetch result at the specified indexes.
- [- enumerateObjectsUsingBlock:](<phfetchresult/enumerateobjects(__).md>) — Executes the specified block using each object in the fetch result, starting with the first object and continuing in order to the last object.
- [- enumerateObjectsWithOptions:usingBlock:](<phfetchresult/enumerateobjects(options_using_).md>) — Executes the specified block using each object in the fetch result.

## See Also

### Asset retrieval

- [Fetching Objects and Requesting Changes](../photokit/fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [PHAsset](phasset.md) — A representation of an image, video, or Live Photo in the Photos library.
- [PHAssetCollection](phassetcollection.md) — A representation of a Photos asset grouping, such as a moment, user-created album, or smart album.
- [PHCollection](phcollection.md) — The abstract superclass for Photos asset collections and collection lists.
- [PHCollectionList](phcollectionlist.md) — A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [PHObject](phobject.md) — The abstract superclass for Photos model objects (assets and collections).
- [PHFetchOptions](phfetchoptions.md) — A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.

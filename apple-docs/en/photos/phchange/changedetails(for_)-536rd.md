---
title: 'changeDetails(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.13+, tvOS 10.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phchange/changedetails(for:)-536rd'
source_url: 'https://developer.apple.com/documentation/photos/phchange/changedetails(for:)-536rd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phchange/changedetails%28for%3A%29-536rd.json'
content_hash: 'sha256:d0cae9d4aeff2f82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHChange](../phchange.md)

# changeDetails(for:)

<sub>Instance Method</sub>

Returns detailed change information for the specified asset or collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func changeDetails<T>(for object: T) -> PHObjectChangeDetails<T>? where T : PHObject
```

## Parameters

- `object` — A [PHAsset](../phasset.md), [PHAssetCollection](../phassetcollection.md), or [PHCollectionList](../phcollectionlist.md) object.

## Return Value

A change details object, or `nil` if there have been no changes to the specified asset or collection.

## Discussion

When Photos calls your change observer’s [- photoLibraryDidChange:](<../phphotolibrarychangeobserver/photolibrarydidchange(__).md>) method, call this [changeDetails(for:)](<changedetails(for_)-536rd.md>) method to get detailed change information about an asset or collection you’ve previously fetched. If the asset or collection has changed since you last fetched it, the resulting [PHObjectChangeDetails](../phobjectchangedetails.md) object describes the changes. If there are no changes between the fetched object and the current state of the asset or collection it represents in the Photos library, this method returns `nil`.

For an asset collection or collection list, this method and the [PHObjectChangeDetails](../phobjectchangedetails.md) object it returns describe only changes to the collection’s properties. If you are instead interested in changes to the collection’s membership, use the [changeDetails(for:)](<changedetails(for_)-2fne7.md>) method.

## See Also

### Getting Change Details

- [changeDetails(for:)](<changedetails(for_)-33a6n.md>)
- [changeDetails(for:)](<changedetails(for_)-2fne7.md>) — Returns detailed change information for a fetch result.

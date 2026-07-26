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
doc_path: '/documentation/photos/phchange/changedetails(for:)-2fne7'
source_url: 'https://developer.apple.com/documentation/photos/phchange/changedetails(for:)-2fne7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phchange/changedetails%28for%3A%29-2fne7.json'
content_hash: 'sha256:91cce78cf6cc8205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHChange](../phchange.md)

# changeDetails(for:)

<sub>Instance Method</sub>

Returns detailed change information for a fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func changeDetails<T>(for fetchResult: PHFetchResult<T>) -> PHFetchResultChangeDetails<T>? where T : PHObject
```

## Parameters

- `fetchResult` — A Photos fetch result.

## Return Value

A change details object, or `nil` if there have been no changes affecting the fetch result’s contents.

## Discussion

When Photos calls your change observer’s [- photoLibraryDidChange:](<../phphotolibrarychangeobserver/photolibrarydidchange(__).md>) method, call this [changeDetails(for:)](<changedetails(for_)-2fne7.md>) method to get detailed change information about the results of a fetch you’ve previously performed. If there have been any changes in the Photos library affecting the fetch, the resulting [PHFetchResultChangeDetails](../phfetchresultchangedetails.md) object tells you if any contents in the fetch result have been added, removed, or changed since you fetched it. If there have been no changes since you performed the fetch, this method returns `nil`.

Typically, if your app displays the members of a collection (such as an album or moment), you use a method such as [+ fetchAssetsInAssetCollection:options:](<../phasset/fetchassets(in_options_).md>) to retrieve those members and then keep the resulting [PHFetchResult](../phfetchresult.md) object. You can then pass that fetch result to this method to learn about changes to the collection, such as whether new members have been added to it (and which indexes to insert them at in your UI).

To find out about changes to an object’s properties, such as a collection’s title or an asset’s metadata, use the [changeDetails(for:)](<changedetails(for_)-536rd.md>) method.

## See Also

### Getting Change Details

- [changeDetails(for:)](<changedetails(for_)-33a6n.md>)
- [changeDetails(for:)](<changedetails(for_)-536rd.md>) — Returns detailed change information for the specified asset or collection.

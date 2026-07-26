---
title: 'fetchMoments(inMomentList:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+, tvOS 10.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phassetcollection/fetchmoments(inmomentlist:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/fetchmoments(inmomentlist:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/fetchmoments%28inmomentlist%3Aoptions%3A%29.json'
content_hash: 'sha256:2fff222402bf42b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# fetchMoments(inMomentList:options:)

<sub>Type Method</sub>

Retrieves asset collections in the specified moment list collection.

> [!warning] Deprecated
> Will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func fetchMoments(inMomentList momentList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

## Parameters

- `momentList` — A collection list whose type is [PHCollectionListTypeMomentList](../phcollectionlisttype/momentlist.md).

- `options` — Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAssetCollection](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## Discussion

The Photos app automatically creates moments to group assets by time and location, and also creates moment lists to group related moments. Moment lists have two subtypes: a moment cluster groups a few related moments, and a moment year groups all moments in a calendar year.

## See Also

### Fetching Asset Collections

- [+ fetchAssetCollectionsWithLocalIdentifiers:options:](<fetchassetcollections(withlocalidentifiers_options_).md>) — Retrieves asset collections with the specified unique identifiers.
- [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) — Retrieves asset collections of the specified type and subtype.
- [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) — Retrieves asset collections of the specified type containing the specified asset.
- [+ fetchAssetCollectionsWithALAssetGroupURLs:options:](<fetchassetcollections(withalassetgroupurls_options_).md>) — Retrieves asset collections using URLs provided by the Assets Library framework. _(deprecated)_
- [+ fetchMomentsWithOptions:](<fetchmoments(with_).md>) — Retrieves asset collections corresponding to moments seen in the Photos app. _(deprecated)_

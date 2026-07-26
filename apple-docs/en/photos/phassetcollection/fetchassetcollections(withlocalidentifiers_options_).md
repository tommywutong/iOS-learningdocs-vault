---
title: 'fetchAssetCollections(withLocalIdentifiers:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollection/fetchassetcollections(withlocalidentifiers:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/fetchassetcollections(withlocalidentifiers:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/fetchassetcollections%28withlocalidentifiers%3Aoptions%3A%29.json'
content_hash: 'sha256:2be315721e55ec60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# fetchAssetCollections(withLocalIdentifiers:options:)

<sub>Type Method</sub>

Retrieves asset collections with the specified unique identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchAssetCollections(withLocalIdentifiers identifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

## Parameters

- `identifiers` — An array of `NSString` objects, each the [localIdentifier](../phobject/localidentifier.md) string of an asset collection.

- `options` — Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAssetCollection](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## See Also

### Fetching Asset Collections

- [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) — Retrieves asset collections of the specified type and subtype.
- [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) — Retrieves asset collections of the specified type containing the specified asset.
- [+ fetchAssetCollectionsWithALAssetGroupURLs:options:](<fetchassetcollections(withalassetgroupurls_options_).md>) — Retrieves asset collections using URLs provided by the Assets Library framework. _(deprecated)_
- [+ fetchMomentsInMomentList:options:](<fetchmoments(inmomentlist_options_).md>) — Retrieves asset collections in the specified moment list collection. _(deprecated)_
- [+ fetchMomentsWithOptions:](<fetchmoments(with_).md>) — Retrieves asset collections corresponding to moments seen in the Photos app. _(deprecated)_

---
title: 'fetchMomentLists(with:containingMoment:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+, tvOS 10.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phcollectionlist/fetchmomentlists(with:containingmoment:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist/fetchmomentlists(with:containingmoment:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist/fetchmomentlists%28with%3Acontainingmoment%3Aoptions%3A%29.json'
content_hash: 'sha256:babb904d99d2b023'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionList](../phcollectionlist.md)

# fetchMomentLists(with:containingMoment:options:)

<sub>Type Method</sub>

Retrieves collection lists of the specified moment list type containing the specified moment.

> [!warning] Deprecated
> Will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func fetchMomentLists(with momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

## Parameters

- `momentListSubtype` — The type of moment list, either [PHCollectionListSubtypeMomentListCluster](../phcollectionlistsubtype/momentlistcluster.md) or [PHCollectionListSubtypeMomentListYear](../phcollectionlistsubtype/momentlistyear.md). See [PHCollectionListSubtype](../phcollectionlistsubtype.md).

- `moment` — An asset collection whose type is [PHAssetCollectionTypeMoment](../phassetcollectiontype/moment.md).

- `options` — Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHCollectionList](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

## Discussion

The Photos app automatically creates moments to group assets by time and location, and also creates moment lists to group related moments. Moment lists have two subtypes: a moment cluster groups a few related moments, and a moment year groups all moments in a calendar year.

## See Also

### Fetching Collection Lists

- [+ fetchCollectionListsContainingCollection:options:](<fetchcollectionlistscontaining(__options_).md>) — Retrieves collection lists that contain the specified collection.
- [+ fetchCollectionListsWithLocalIdentifiers:options:](<fetchcollectionlists(withlocalidentifiers_options_).md>) — Retrieves collection lists with the specified local-device-specific unique identifiers.
- [+ fetchCollectionListsWithType:subtype:options:](<fetchcollectionlists(with_subtype_options_).md>) — Retrieves collection lists of the specified type.
- [+ fetchMomentListsWithSubtype:options:](<fetchmomentlists(with_options_).md>) — Retrieves collection lists of the specified moment list type. _(deprecated)_

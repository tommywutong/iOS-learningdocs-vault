---
title: 'transientAssetCollection(withAssetFetchResult:title:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollection/transientassetcollection(withassetfetchresult:title:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/transientassetcollection(withassetfetchresult:title:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/transientassetcollection%28withassetfetchresult%3Atitle%3A%29.json'
content_hash: 'sha256:c028f4aa6ee0f9c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# transientAssetCollection(withAssetFetchResult:title:)

<sub>Type Method</sub>

Creates a temporary asset collection containing the assets from the specified fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func transientAssetCollection(withAssetFetchResult fetchResult: PHFetchResult<PHAsset>, title: String?) -> PHAssetCollection
```

## Parameters

- `fetchResult` — A fetch result containing one or more [PHAsset](../phasset.md) objects.

- `title` — A name for the new temporary asset collection.

## Return Value

A new asset collection.

## Discussion

Transient asset collections are not saved to local storage or iCloud and do not appear in the Photos application or other apps using the Photos framework. A transient collection can be useful if you’ve designed a UI for displaying the contents of a collection and want to display an arbitrary set of assets.

## See Also

### Creating Temporary Asset Collections

- [+ transientAssetCollectionWithAssets:title:](<transientassetcollection(with_title_).md>) — Creates a temporary asset collection containing the specified assets.

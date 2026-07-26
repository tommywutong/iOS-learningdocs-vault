---
title: predicate
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchoptions/predicate
source_url: 'https://developer.apple.com/documentation/photos/phfetchoptions/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchoptions/predicate.json'
content_hash: 'sha256:7ecde06eab92b4d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchOptions](../phfetchoptions.md)

# predicate

<sub>Instance Property</sub>

A predicate that specifies which properties to select results by and that also specifies any constraints on selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var predicate: NSPredicate? { get set }
```

## Discussion

Construct a predicate with the properties of the class of objects that you want to fetch, listed in the [PHFetchOptions](../phfetchoptions.md) table. For example, the following code uses a predicate to fetch assets matching a specific set of [mediaSubtypes](../phasset/mediasubtypes.md) values.

**Swift**

```swift
let format = "(mediaSubtypes & %d) != 0 || (mediaSubtypes & %d) != 0"
let fetchOptions = PHFetchOptions()
fetchOptions.predicate = NSPredicate(format: format,
                                     argumentArray: [PHAssetMediaSubtype.photoPanorama, PHAssetMediaSubtype.videoHighFrameRate])
        
let fetchResult = PHAsset.fetchAssets(with: PHAssetMediaType.image,
                                          options: fetchOptions)
```

**Objective-C**

```objc
NSString *format = @"(mediaSubtypes & %d) != 0 || (mediaSubtypes & %d) != 0";
PHFetchOptions* fetchOptions = [PHFetchOptions new];
fetchOptions.predicate = [NSPredicate predicateWithFormat:format,
                          PHAssetMediaSubtypePhotoPanorama,
                          PHAssetMediaSubtypeVideoHighFrameRate];

PHFetchResult* fetchResult = [PHAsset fetchAssetsWithOptions:fetchOptions];
```

Photos does not support predicates created with the `NSPredicate` method `init` or the `predicateWithBlock` method.

## See Also

### Sorting and Filtering Fetch Results

- [sortDescriptors](sortdescriptors.md) — A list of sort descriptors, specifying an order for the fetched objects.

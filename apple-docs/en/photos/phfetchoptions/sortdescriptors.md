---
title: sortDescriptors
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchoptions/sortdescriptors
source_url: 'https://developer.apple.com/documentation/photos/phfetchoptions/sortdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchoptions/sortdescriptors.json'
content_hash: 'sha256:b539cc3e81e5c095'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchOptions](../phfetchoptions.md)

# sortDescriptors

<sub>Instance Property</sub>

A list of sort descriptors, specifying an order for the fetched objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sortDescriptors: [NSSortDescriptor]? { get set }
```

## Discussion

Construct sort descriptors with the properties of the objects that you want to fetch, listed in the [PHFetchOptions](../phfetchoptions.md) table. For example, the following code sorts by creation date to find the oldest asset in the photo library.

**Swift**

```swift
let fetchOptions = PHFetchOptions()
fetchOptions.sortDescriptors = [NSSortDescriptor(key: "creationDate", ascending: true)]
let fetchResult = PHAsset.fetchAssets(with: fetchOptions)
return fetchResult.firstObject
```

**Objective-C**

```objc
PHFetchOptions *fetchOptions = [PHFetchOptions new];
fetchOptions.sortDescriptors = @[
    [NSSortDescriptor sortDescriptorWithKey:@"creationDate" ascending:YES],
];
PHFetchResult *fetchResult = [PHAsset fetchAssetsWithOptions:fetchOptions];
return [fetchResult firstObject];
```

## See Also

### Sorting and Filtering Fetch Results

- [predicate](predicate.md) — A predicate that specifies which properties to select results by and that also specifies any constraints on selection.

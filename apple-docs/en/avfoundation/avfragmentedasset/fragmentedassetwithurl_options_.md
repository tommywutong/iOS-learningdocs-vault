---
title: 'fragmentedAssetWithURL:options:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avfragmentedasset/fragmentedassetwithurl:options:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedasset/fragmentedassetwithurl:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedasset/fragmentedassetwithurl%3Aoptions%3A.json'
content_hash: 'sha256:ccf387c0a98c29a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedAsset](../avfragmentedasset.md)

# fragmentedAssetWithURL:options:

<sub>Type Method</sub>

Creates a fragmented asset for the media at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) fragmentedAssetWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `URL` — A URL that points to the desired media resource.

- `options` — A dictionary of keys for specifying initialization options. Valid values are [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) and [AVURLAssetReferenceRestrictionsKey](../avurlassetreferencerestrictionskey.md).

## Return Value

A fragmented asset that models the media at the specified URL.

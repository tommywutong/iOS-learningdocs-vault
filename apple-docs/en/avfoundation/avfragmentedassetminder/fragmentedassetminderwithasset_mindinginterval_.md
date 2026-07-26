---
title: 'fragmentedAssetMinderWithAsset:mindingInterval:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avfragmentedassetminder/fragmentedassetminderwithasset:mindinginterval:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/fragmentedassetminderwithasset:mindinginterval:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedassetminder/fragmentedassetminderwithasset%3Amindinginterval%3A.json'
content_hash: 'sha256:13955ba606dd5e92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedAssetMinder](../avfragmentedassetminder.md)

# fragmentedAssetMinderWithAsset:mindingInterval:

<sub>Type Method</sub>

Creates a fragmented asset minder containing the specified asset and minding interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) fragmentedAssetMinderWithAsset:(AVAsset<AVFragmentMinding> *) asset mindingInterval:(NSTimeInterval) mindingInterval;
```

## Parameters

- `asset` — The fragmented asset added to the fragmented asset minder.

- `mindingInterval` — The amount of time between checking to see if the system appended additional fragments to the minded asset.

## Return Value

The new fragmented asset minder.

## See Also

### Creating an asset minder

- [- initWithAsset:mindingInterval:](<init(asset_mindinginterval_).md>) — Creates a fragmented asset minder that monitors the specified asset at the indicated minding interval.

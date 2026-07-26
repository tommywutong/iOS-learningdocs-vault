---
title: 'init(asset:mindingInterval:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avfragmentedassetminder/init(asset:mindinginterval:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/init(asset:mindinginterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedassetminder/init%28asset%3Amindinginterval%3A%29.json'
content_hash: 'sha256:e66b56c90eae09d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedAssetMinder](../avfragmentedassetminder.md)

# init(asset:mindingInterval:)

<sub>Initializer</sub>

Creates a fragmented asset minder that monitors the specified asset at the indicated minding interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(asset: any AVAsset & AVFragmentMinding, mindingInterval: TimeInterval)
```

## Parameters

- `asset` — The fragmented asset added to the fragmented asset minder.

- `mindingInterval` — The amount of time between checking to see if the system appended additional fragments to the minded asset.

## Return Value

The new fragmented asset minder.

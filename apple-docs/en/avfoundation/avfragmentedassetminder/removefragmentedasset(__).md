---
title: 'removeFragmentedAsset(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avfragmentedassetminder/removefragmentedasset(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/removefragmentedasset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedassetminder/removefragmentedasset%28_%3A%29.json'
content_hash: 'sha256:194971aba0f975f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedAssetMinder](../avfragmentedassetminder.md)

# removeFragmentedAsset(_:)

<sub>Instance Method</sub>

Removes a fragmented asset from the array of minded assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeFragmentedAsset(_ asset: any AVAsset & AVFragmentMinding)
```

## Parameters

- `asset` — The fragmented asset to remove from the minder.

## See Also

### Adding and removing fragmented assets

- [- addFragmentedAsset:](<addfragmentedasset(__).md>) — Adds a fragmented asset to the array of minded assets.

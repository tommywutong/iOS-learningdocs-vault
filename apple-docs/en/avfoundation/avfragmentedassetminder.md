---
title: AVFragmentedAssetMinder
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avfragmentedassetminder
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedassetminder.json'
content_hash: 'sha256:00f06be9ca1bb011'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVFragmentedAssetMinder

<sub>Class</sub>

An object that periodically checks whether the system adds new fragments to a fragmented asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVFragmentedAssetMinder
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVFragmentedMovieMinder](avfragmentedmovieminder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an asset minder

- [- initWithAsset:mindingInterval:](<avfragmentedassetminder/init(asset_mindinginterval_).md>) — Creates a fragmented asset minder that monitors the specified asset at the indicated minding interval.

### Configuring the minding interval

- [mindingInterval](avfragmentedassetminder/mindinginterval.md) — An interval that specifies when to perform a check for additional fragments.

### Inspecting a fragment asset

- [assets](avfragmentedassetminder/assets.md) — The minded array of fragmented assets.

### Adding and removing fragmented assets

- [- addFragmentedAsset:](<avfragmentedassetminder/addfragmentedasset(__).md>) — Adds a fragmented asset to the array of minded assets.
- [- removeFragmentedAsset:](<avfragmentedassetminder/removefragmentedasset(__).md>) — Removes a fragmented asset from the array of minded assets.

## See Also

### Fragmented assets

- [AVFragmentedAsset](avfragmentedasset.md) — An asset with a duration that the system can extend without modifying its existing media data.
- [AVFragmentedAssetTrack](avfragmentedassettrack.md) — An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [AVFragmentMinding](avfragmentminding.md) — A protocol that defines whether an asset supports fragment minding.

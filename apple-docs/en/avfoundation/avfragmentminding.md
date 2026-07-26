---
title: AVFragmentMinding
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avfragmentminding
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentminding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentminding.json'
content_hash: 'sha256:ec31256d01ffeff2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVFragmentMinding

<sub>Protocol</sub>

A protocol that defines whether an asset supports fragment minding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVFragmentMinding
```

## Relationships

- **Conforming Types**: [AVFragmentedAsset](avfragmentedasset.md), [AVFragmentedMovie](avfragmentedmovie.md)

## Topics

### Fragment minder association

- [associatedWithFragmentMinder](avfragmentminding/isassociatedwithfragmentminder.md) — A Boolean value that indicates whether an asset that supports fragment minding is currently associated with a fragment minder.

## See Also

### Fragmented assets

- [AVFragmentedAsset](avfragmentedasset.md) — An asset with a duration that the system can extend without modifying its existing media data.
- [AVFragmentedAssetTrack](avfragmentedassettrack.md) — An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [AVFragmentedAssetMinder](avfragmentedassetminder.md) — An object that periodically checks whether the system adds new fragments to a fragmented asset.

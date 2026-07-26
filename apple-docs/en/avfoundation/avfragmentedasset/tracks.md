---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+（16.0 起废弃）, iPadOS 12.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 12.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avfragmentedasset/tracks
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedasset/tracks.json'
content_hash: 'sha256:0667777076aa80f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedAsset](../avfragmentedasset.md)

# tracks

<sub>Instance Property</sub>

The tracks an asset contains.

> [!warning] Deprecated
> Load the value of [tracks](../avpartialasyncproperty/tracks-9z3j9.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tracks: [AVFragmentedAssetTrack] { get }
```

## See Also

### Accessing tracks

- [- trackWithTrackID:](<track(withtrackid_).md>) — Returns a track that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Returns tracks that present media of a specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that present media of a specified characteristic. _(deprecated)_

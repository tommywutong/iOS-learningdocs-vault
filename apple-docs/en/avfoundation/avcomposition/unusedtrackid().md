---
title: unusedTrackID()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/unusedtrackid()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/unusedtrackid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/unusedtrackid%28%29.json'
content_hash: 'sha256:e3f0828ea77a89a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# unusedTrackID()

<sub>Instance Method</sub>

Returns an identifier that no other tracks in the asset use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unusedTrackID() -> CMPersistentTrackID
```

## Return Value

An unused [CMPersistentTrackID](../../coremedia/cmpersistenttrackid.md) value.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a composition contains.
- [- trackWithTrackID:](<track(withtrackid_).md>) — Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that contain media of a specified characteristic.
